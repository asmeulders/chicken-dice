from .Dice import Dice
from .Side import Side

class Hand():
    def __init__(self, die, num_die=0) -> None:
        self.die = die
        self.num_die = num_die
        self.num_total_die = len(die) * num_die
        self.die_store: dict[int, dict] = self.reset()

    def init_die_store(self, quantities):
        return {
            dice.get_rank(): {
                "num_die": q,
                "dice": dice
            } for dice, q in zip(self.die, quantities)
        }

    def reset(self):
        quantities = [self.num_die]
        quantities.extend([0] * (len(self.die) - 1))
        return self.init_die_store(quantities)

    def get_die(self) -> list[Dice]:
        return self.die

    def get_num_total_die(self) -> int:
        return self.num_total_die

    def get_num_die(self) -> int:
            return self.num_die

    def roll_die(self) -> list[Side]:
        results = []
        for die_dict in self.die_store.values():
            for _ in range(die_dict["num_die"]):
                results.append(die_dict["dice"].roll())
        return results

    def add_dice(self, dice: Dice) -> None:
        self.die_store[dice.get_rank()]["num_die"] += 1

    def remove_dice(self, dice: Dice) -> None:
        self.die_store[dice.get_rank()]["num_rnum_dieank"] -= 1

    def __len__(self):
        length = 0
        for dice_data in self.die_store.values():
            length += dice_data["num_die"]
        return length

class EmptyHand(Hand):
    def __init__(self):
        super().__init__([])