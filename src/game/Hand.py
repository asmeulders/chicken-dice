from Dice import Dice
from Side import Side

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

    def remove_dice(self, dice: Dice) -> bool:
        """Returns true if dice was removed, false if not."""
        try:
            list.remove(self.die, dice)
            return True
        except ValueError:
            return False


class EmptyHand(Hand):
    def __init__(self):
        super().__init__([])