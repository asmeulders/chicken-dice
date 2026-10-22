import random

from src.game.Side import Side, EmptySide, EggSide, ChickenSide, FoxSide


class Dice:
    """A class that defines how a general die works in the game Chicken!"""
    def __init__(self, num_sides: int, chicken: list[int], foxes: list[int], eggs: list[int], rank: int) -> None:
        """
        We expect chicken, foxes, and eggs to be list of ints containing the quantity values of each of the
        sides.
        rank is hierarchy of which to start with. cannot be negative. start at 0, then go up
        """
        if len(chicken) + len(foxes) + len(eggs) > num_sides:
            raise ValueError

        self.num_sides = num_sides
        self.sides = []

        self.set_rank(rank)
    
        for e in eggs:
            self.sides.append(EggSide(e))

        for c in chicken:
            self.sides.append(ChickenSide(c))

        for f in foxes:
            self.sides.append(FoxSide(f))

        num_empty = num_sides - (len(chicken) + len(foxes) + len(eggs))
        for _ in range(num_empty):
            self.sides.append(EmptySide())

    def set_rank(self, rank):
        if not isinstance(rank, int):
            raise TypeError
        if rank < 0:
            raise ValueError

        self.rank = rank

    def get_num_sides(self) -> int:
        return self.num_sides

    def get_sides(self) -> list[Side]:
        return self.sides

    def get_rank(self) -> int:
        return self.rank

    def roll(self) -> Side:
        return random.choice(self.sides)

    def __eq__(self, other):
        if not isinstance(other, Dice):
            raise NotImplemented

        return self.num_sides == other.get_num_sides() and self.sides == other.get_sides()
        
class WhiteDice(Dice):
    def __init__(self) -> None:
        chicken = [1, 1]
        eggs = [1, 1]
        foxes = [1]

        super().__init__(num_sides=6, chicken=chicken, foxes=foxes, eggs=eggs, rank=0)

class YellowDice(Dice):
    def __init__(self) -> None:
        chicken = [1, 1, 1]
        eggs = [1]
        foxes = [1]

        super().__init__(num_sides=6, chicken=chicken, foxes=foxes, eggs=eggs, rank=1)

class OrangeDice(Dice):
    def __init__(self) -> None:
        chicken = [2, 1]
        eggs = []
        foxes = [1, 1]

        super().__init__(num_sides=6, chicken=chicken, foxes=foxes, eggs=eggs, rank=2)