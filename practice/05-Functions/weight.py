"""
Gravity works differently in Zortan, use the following formula
to see how much you weight on Zortan.

Zortan Weight = (Earth Weight + 32) / 8
"""


def calcWeight(weight: float) -> float:
    return (weight + 32) / 8


print(f"Your weight {calcWeight(60):.2f} kgs on Zortan")
