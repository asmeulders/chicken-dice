from enum import Enum

class SideValues(Enum):
    EMPTY = 1
    EGG = 2
    CHICKEN = 3
    FOX = 4

class Side():
    def __init__(self, side_value: SideValues, quantity: int):
        if quantity < 0:
            raise ValueError

        self.value = side_value
        self.quantity = quantity

    def get_value(self):
        return self.value

    def get_quantity(self):
        return self.quantity

class EmptySide(Side):
    def __init__(self):
        super().__init__(SideValues.EMPTY, quantity=0)

class EggSide(Side):
    def __init__(self, quantity):
        super().__init__(SideValues.EGG, quantity=quantity)

class ChickenSide(Side):
    def __init__(self, quantity):
        super().__init__(SideValues.CHICKEN, quantity=quantity)

class FoxSide(Side):
    def __init__(self, quantity):
        super().__init__(SideValues.FOX, quantity=quantity)
