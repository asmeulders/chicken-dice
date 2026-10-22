from .Agent import Agent
from src.game.Action import Action

class DummyAgent(Agent):
    def choose_action(self) -> Action:
        return Action.PASS