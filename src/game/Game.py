from .Dice import Dice, WhiteDice, YellowDice, OrangeDice
from .Player import Player
from .Hand import Hand, EmptyHand
from .Action import Action
from .Side import SideValues

from src.agents.Agent import Agent
from src.agents.RandomAgent import RandomAgent
from src.agents.DummyAgent import DummyAgent

class Game():
    """
    players > 0
    die: 4 white, 4 yellow, 4 orange in classic
    game loop:
        1. player rolls die
        2. count up result and keep track of running chicken/fox
        3. go until player decides to stop, gets 3 foxes, or wins
        4. add die according to how many eggs show up
        5. player rerolls anything not a chicken or a fox
        6. once next player goes then repeat

    total_die, current_die, current_chicken, current_fox, player_order, active_player, 
    turn, 
    """
    def __init__(self, goal: int, agents: list[Agent], die: list[Dice], num_die: int, fox_limit: int) -> None:
        """
        die is a list of unique types of die in order of rank (0 is lowest and goes in hand first)
        num_die = die per unique type
        check die rank for ordering
        """

        # game status
        if not isinstance(goal, int):
            raise TypeError("Goal must be an int")
        if goal < 1:
            raise ValueError("Goal but be at least one")
        self.goal: int = goal
        if not isinstance(fox_limit, int):
            raise TypeError("Fox limit must be an int")
        if fox_limit < 1:
            raise ValueError("Fox limit but be at least one")
        self.fox_limit: int = fox_limit
        self.current_points: int = 0
        self.current_fox: int = 0
        self.turn: int = 0

        # players
        if not isinstance(agents, list):
            raise TypeError("agents must be a list of agents")
        if len(agents) < 2:
            raise ValueError("Need at least 2 players")

        self.num_players: int = len(agents)
        self.players: list[Player] = []
        self.initialize_players(agents)

        # active player
        self.active_player = None
        self.active_player_id: int = -1

        # dice
        self.die = die
        self.dice_pile: list[Dice] = []
        self.num_die = num_die
        self.num_total_die = len(die) * num_die
        self.initialize_rank_dict(die)
        self.hand = Hand([])
        print("Made game")


    # =================================================================
    # ------- Accessors -----------------------------------------------
    # =================================================================

    def get_turn(self) -> int:
        return self.turn

    def get_goal(self) -> int:
        return self.goal

    def get_num_players(self) -> int:
        return self.num_players
    
    def get_players(self) -> list[Player]:
        return self.players
    
    def get_die(self) -> list[Dice]:
        return self.die

    # =================================================================
    # ------- Mutators ------------------------------------------------
    # =================================================================

    def initialize_players(self, agents):
        for i, agent in enumerate(agents):
            if not isinstance(agent, Agent):
                raise TypeError("agents must be a list of agents")
            
            self.players.append(Player(i, agent))

    def initialize_rank_dict(self, die):
        self.rank_dict = {
            dice.get_rank(): {
                "num_die": 0,
                "dice": dice
            } for dice in die
        }
    
    def initialize_hand(self):
        """
        rank_dict = {
            {rank}: {
                num_die: # in hand for this type,
                dice: dice object
            }
        }
        """
        for rank, num_die in self.rank_dict.items():
            assert isinstance(num_die, int)
            for _ in range(num_die):
                if not self.hand.add_dice(self.rank_dict[rank]["dice"]):
                    raise Exception("Dice was not added")


    # =================================================================
    # ------- Game Functions ------------------------------------------
    # =================================================================

    def start_game(self):
        print("Start game")
        self.reset_all_die() # resets the rank_dict and initializes the hand
        self.start_turn() # set first active player and give them their hand

        assert isinstance(self.active_player, Player)

        # game loop
        while not self.game_over():
            action = self.active_player.get_action()
            print(f"Player {self.active_player_id}: {"Roll" if action == Action.ROLL else "Pass"}")
            self.apply_action(action)

        # clean up

    def apply_action(self, action):
        if action == Action.ROLL:
            sides = self.hand.roll_die()
            for s in sides:
                if s.get_value() == SideValues.CHICKEN:
                    assert isinstance(self.active_player, Player) # figure out how to get types without assert
                    self.current_points += s.get_quantity()
                elif s.get_value() == SideValues.EGG:
                    self.do_egg_action()
                elif s.get_value() == SideValues.FOX:
                    self.current_fox += s.get_quantity()

        elif action == Action.PASS:
            self.end_turn(is_foxed=False)

        else:
            raise ValueError("Invalid action")

        if self.current_fox >= self.fox_limit:
            self.end_turn(is_foxed=True)

    def do_egg_action(self):
        dice = self.dice_pile.pop()
        self.hand.add_dice(dice)
        self.rank_dict[dice.get_rank()]["num_die"] += 1
        
    def reset_all_die(self):
        """
        Reset the rank_dict, initialize the hand, and reset dice pile.
        """
        self.reset_rank_dict()
        self.initialize_hand()
        self.reset_dice_pile()

    def reset_rank_dict(self):
        self.rank_dict[0]["num_die"] = self.num_die
        num_ranks = int(self.num_total_die / self.num_die)
        for rank in range(1, num_ranks):
            self.rank_dict[rank]["num_die"] = 0

    def reset_dice_pile(self) -> list[Dice]:
        if len(self.die) <= 1:
            return self.die
        for dice in self.die[1:]:
            for _ in range(self.num_die):
                self.dice_pile.append(dice)
        return self.die

    def start_turn(self):
        if self.active_player_id == -1 or not self.active_player_id:
            self.active_player_id = 0

        print("Start turn", self.active_player_id)            
        self.active_player = self.players[self.active_player_id]
        self.active_player.set_hand(self.hand)

    def end_turn(self, is_foxed):
        assert isinstance(self.active_player, Player)
        assert isinstance(self.active_player_id, int)
        print(f"End turn {self.turn} for player {self.active_player_id}")

        if is_foxed:
            self.reset_all_die()
        else:
            self.active_player.add_points(self.current_points)

        self.current_points = 0
        self.current_fox = 0
        self.active_player.set_hand(EmptyHand)
        self.turn += 1
        self.active_player = (self.active_player_id + 1) % self.num_players
        

    def game_over(self) -> bool:
        """Returns true if the game is over, false if not."""
        for p in self.players:
            if p.get_score() >= self.get_goal():
                print("Game over")
                return True
            
        return False

def main():
    agents = [RandomAgent(), RandomAgent(), DummyAgent()]
    die = [WhiteDice(), YellowDice(), OrangeDice()]
    game = Game(goal=25, agents=agents, die=die, num_die=4, fox_limit=3)

    game.start_game()

    for player in game.get_players():
        print(f"Player {player.get_player_id()} Score: {player.get_score()}")

if __name__ == "__main__":
    main()