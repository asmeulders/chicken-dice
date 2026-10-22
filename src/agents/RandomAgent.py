import random

from Agent import Agent
from src.game.Action import Action

class RandomAgent(Agent):
    def __init__(self):
        pass

    def choose_action(self) -> Action:
        return random.choice([Action.PASS, Action.ROLL])