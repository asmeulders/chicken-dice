from Dice import Dice, WhiteDice, YellowDice, OrangeDice
from Player import Player
from Hand import Hand

def Game():
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
    def __init__(self, goal: int, num_players: int, die: list[Dice]) -> None:
        """
        die is a list of unique types of die
        num_die = die per unique type
        check die rank for ordering
        """
        self.turn = 0
        self.goal = goal

        self.num_players = num_players
        self.initialize_players()
        self.active_player = 0
        self.die = die
        self.active_die = []

    def initialize_players(self):
        self.players = []
        for i in range(self.num_players):
            self.players.append(Player(i))

    def initialize_hand():
        pass

    def get_turn(self) -> int:
        return self.turn

    def get_goal(self) -> int:
        return self.goal

    def game_over(self) -> bool:
        """Returns true if the game is over, false if not."""
        for p in self.players:
            if p.get_score() >= self.get_goal():
                return True
            
        return False

    def get_num_players(self) -> int:
        return self.num_players
    
    def get_players(self) -> list[Player]:
        return self.players
    
    def get_die(self) -> list[Dice]:
        return self.die

    def end_turn(self):
        self.turn += 1
        self.active_player = (self.active_player + 1) % self.num_players
        self.players[self.active_player].set_hand(Hand(self.die))

    def start_game(self):
        pass