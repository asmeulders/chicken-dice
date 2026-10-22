from .Agent import Agent
from src.game.Action import Action

class RollAgent(Agent):
    def choose_action(self) -> Action:
        return Action.ROLL