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
                "num_active": q,
                "dice": dice
            } for dice, q in zip(self.die, quantities)
        }

    def reset(self):
        quantities = [0] * (len(self.die))
        quantities[0] = self.num_die
        print("quantities", quantities)
        return self.init_die_store(quantities)

    def get_die(self) -> list[Dice]:
        return self.die

    def get_num_total_die(self) -> int:
        return self.num_total_die

    def get_num_die(self) -> int:
        return self.num_die

    def roll_die(self) -> list[tuple[Dice, Side]]:
        print("rolling die", self.die_store.values())
        results = []
        for die_dict in self.die_store.values():
            for _ in range(die_dict["num_active"]):
                side = die_dict["dice"].roll()
                print(side.get_value())
                results.append((die_dict["dice"], side))
        return results

    def add_dice(self, dice: Dice) -> None:
        if self.__len__() < self.num_total_die:
            self.die_store[dice.get_rank()]["num_die"] += 1
            self.die_store[dice.get_rank()]["num_active"] += 1

    def deactivate_dice(self, dice: Dice) -> None:
        self.die_store[dice.get_rank()]["num_active"] -= 1

    def remove_dice(self, dice: Dice) -> None:
        self.die_store[dice.get_rank()]["num_die"] -= 1
        self.die_store[dice.get_rank()]["num_active"] -= 1

    def reset_inactive_die(self):
        for die_val in self.die_store.values():
            die_val["num_active"] = die_val["num_die"]

    def __len__(self):
        length = 0
        for dice_data in self.die_store.values():
            length += dice_data["num_die"]
        return length

# class EmptyHand(Hand):
#     def __init__(self):
#         super().__init__([])