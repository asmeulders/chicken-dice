from src.game.Action import Action
from src.game.Hand import Hand, EmptyHand
from src.agents.Agent import Agent
from src.agents.RandomAgent import RandomAgent

class Player():
    def __init__(self, id: int, agent: Agent):
        self.player_id = id
        self.score = 0
        self.hand = EmptyHand()

        if not isinstance(agent, Agent):
            raise TypeError("agent must be an Agent object")
        self.agent = agent

    # Accessors

    def get_player_id(self) -> int:
        return self.player_id

    def get_score(self) -> int:
        return self.score

    def get_hand(self) -> Hand:
        return self.hand

    def set_hand(self, hand) -> None:
        self.hand = hand

    # Mutators

    def set_score(self, score) -> None:
        if not isinstance(score, int):
            raise TypeError("Score must be an int")
        if score < 0:
            raise ValueError("Score cannot be negative")
        
        self.score = score

    def add_points(self, points) -> int:
        """
        Add points to score and return the new score
        """
        if not isinstance(points, int):
            raise TypeError("Points must be an int")
        if points < 0:
            raise ValueError("Points cannot be negative")
        
        self.score += points
        return self.score

    # Game functions

    def get_action(self) -> Action:
        return self.agent.choose_action()


def main():
    random_agent = RandomAgent()
    mia = Player(1, random_agent)
    mia.set_score(100)
    print("Test score is ", mia.get_score(), "!")


if __name__ == "__main__":
    main()