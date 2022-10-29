"""
Save Zortan:
------------

The war has just intensified, Thanos army has reach Zortan and are going to
fight along with him. With his army, this time Thanos is going to attach Avengers
and the battle is going to be intense!!!

Since, everything is going in real-time, we don't have control over characters,
instead our characters will choose their own fight.

This time each character gets it own structure and defined parameters, so as you
can see our code is getting better and certainly we are going to make is awesome
as we progress with future modules.
"""

# Import requied packages
from typing import Final
from random import randint

Character = dict[str, str | int]

# Super Heroes
IRONMAN: Final[Character] = {"name": "Ironman", "attackPower": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "Black Widow", "attackPower": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attackPower": 190, "life": 750}
HULK: Final[Character] = {"name": "Hulk", "attackPower": 300, "life": 1100}

# Super Villains
THANOS: Final[Character] = {"name": "Thanos", "attackPower": 400, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attackPower": 200, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attackPower": 180, "life": 700}

WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

# All Super Heros & Super Villains
superHeroes: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
superVillains: list[Character] = [THANOS, REDSKULL, PROXIMA]

# Helper variables
heroLife: int = 0
villainLife: int = 0

# Attack
for attack in range(3):
    # Each iteration get a new Hero and Villain
    heroIndex = randint(0, len(superHeroes) - 1)
    villainIndex = randint(0, len(superVillains) - 1)
    # Helper varialbes
    currentSuperHero = superHeroes[heroIndex]
    currentVillain = superVillains[villainIndex]
    # print(currentSuperHero)
    # print(currentVillain)

    # Life
    heroLife += currentSuperHero["life"]
    villainLife += currentSuperHero["life"]
    print(
        f"Attack: {attack + 1} => {currentSuperHero['name']} is going to fight with {currentVillain['name']}"
    )

    # Attack
    heroLife -= currentVillain["attackPower"]
    villainLife -= currentSuperHero["attackPower"]

# Print a nice separating line
print("=" * 70)
print(heroLife, villainLife)

# Win or loose
if heroLife >= villainLife:
    print(WIN_MSG)
else:
    print(LOST_MSG)
