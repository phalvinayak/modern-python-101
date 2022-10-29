"""
ENUM:
-----

This is a very good data structure for creating choices or varieties
"""

from enum import Enum, auto


class PizzaSize(Enum):
    """Different Pizza base size in inches"""

    SMALL = 8
    MEDIUM = 10
    LARGE = 12


choice = PizzaSize.MEDIUM
print(f"One oder for {choice.value} inch Pizza")


class Colors(Enum):
    """T-Shirt color options"""

    RED = "red"
    GREEN = "green"
    ORANGE = "orange"


colorChoice = Colors.RED
print(f"Luois favourite color is {colorChoice.value}")
print(f"One order for {Colors.GREEN.value} T-shirt")


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


print(Role.MANAGER.value)
