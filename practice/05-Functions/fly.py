"""
Since Zortan has less gravity, residents can fly if they weight
less than or equal to 15 kgs in Zortan weight.

Louis wants to see which of his friends can fly.

Info:
-----
Our functions do only one thing at a time, this is called as `Single
Responsibility Principle` and important aspect of programming.
"""

from typing import Final

MAX_FLYING_WEIGHT: Final[float] = 15


def calcWeight(weight: float) -> float:
    """
    Calculates Zortan Weight
    ------------------------

    Look how the function just transforms data, from float to float.
    This is called pure function, as it takes and one argument and
    gives one result
    """
    return (weight + 32) / 8


def canFly(weight: float) -> bool:
    """
    Returns if you can fly
    ----------------------

    This function is a nice example for data transformation, we convert
    float values to boolean values!! Nice isn't it!
    """
    return weight <= MAX_FLYING_WEIGHT


def flyingFriends(friends: dict[str, float]) -> None:
    """
    Displays flying and non-flying friends

    Note:
    -----
    No data transformation here.
    We are printing the output to console, the function doesn't return anything.
    """
    for name, earthWeight in friends.items():
        zortanWeight: float = calcWeight(earthWeight)
        if canFly(zortanWeight):
            print(f"{name}: {zortanWeight} kgs, can fly on Zortan!")
        else:
            print(f"{name}: {zortanWeight} kgs, can only walk on Zortan!")


def main() -> None:
    friends: dict[str, float] = {
        "Cece": 54,
        "Roko": 88,
        "Chicko": 50,
        "Niko": 102,
        "Ziko": 90,
    }
    flyingFriends(friends)


# Invoke the main function
main()
