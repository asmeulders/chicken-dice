from abc import ABC, abstractmethod

from src.game.Action import Action

class Agent(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def choose_action(self) -> Action:
        pass
