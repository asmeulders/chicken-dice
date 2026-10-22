from .Dice import Dice
from .Side import Side

class Hand():
    def __init__(self, die: list[Dice]) -> None:
        self.die = die

    def get_die(self) -> list[Dice]:
        return self.die

    def roll_die(self) -> list[Side]:
        results = []
        for d in self.die:
            results.append(d.roll())
        return results

    def add_dice(self, dice: Dice) -> bool:
        """Returns true if dice was added, false if not."""
        try:
            self.die.append(dice)
            return True
        except ValueError:
            return False

    def remove_dice(self, dice: Dice) -> bool:
        """Returns true if dice was removed, false if not."""
        try:
            list.remove(self.die, dice)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self.die)

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if len(self) != len(other):
            return False
        for i, dice in enumerate(self.die):
            if not dice == other.get_die()[i]:
                return False
            
        return True
            



class EmptyHand(Hand):
    def __init__(self):
        super().__init__([])