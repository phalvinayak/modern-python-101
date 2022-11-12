"""
Save Zortan:
------------

Let's convert the game logic into small functions.

Principles:
-----------

1. DRY - Don't Repeat Yourself -
================================
Try to keep your code as DRY as possible, group common functionality into
individual functions.

2. SRP - Single Responsibility Principle -
==========================================
Ideally one function should be responsible for only one operation.

Note:
-----
We will also learn about global & local scope of variables (Using scratch pad)
"""

# Import requied packages
from typing import Final
from random import randint

# -------------------------- Life --------------------------------
Character = dict[str, str | int]

# Helper variables
heroLife: int = 0
villainLife: int = 0


def incHeroLife(life: int) -> None:
    """Increment hero life"""
    global heroLife
    heroLife += life


def incVillainLife(life: int) -> None:
    """Increment villain life"""
    global villainLife
    villainLife += life


def decHeroLife(life: int) -> None:
    """Decrement hero life"""
    global heroLife
    heroLife -= life


def decVillainLife(life: int) -> None:
    """Decrement hero life"""
    global villainLife
    villainLife -= life


# -------------------------- Superheroes --------------------------------
def getAllSuperheros() -> list[Character]:
    # Super Heroes
    IRONMAN: Character = {"name": "Ironman", "attackPower": 250, "life": 1000}
    BLACKWIDOW: Character = {"name": "Black Widow", "attackPower": 180, "life": 800}
    SPIDERMAN: Character = {"name": "Spiderman", "attackPower": 190, "life": 750}
    HULK: Character = {"name": "Hulk", "attackPower": 300, "life": 1100}

    superheroes: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return superheroes


def getSuperhero(index: int) -> Character | None:
    """Returns superhero from the given index"""
    superheroes = getAllSuperheros()
    if index < len(superheroes):
        return superheroes[index]
    else:
        return None


# -------------------------- Villains --------------------------------
def getAllVillains() -> list[Character]:
    # Super Villains
    THANOS: Final[Character] = {"name": "Thanos", "attackPower": 400, "life": 1500}
    REDSKULL: Final[Character] = {"name": "Redskull", "attackPower": 200, "life": 800}
    PROXIMA: Final[Character] = {"name": "Proxima", "attackPower": 180, "life": 700}

    villains: list[Character] = [THANOS, REDSKULL, PROXIMA]
    return villains


def getVillain(index: int) -> Character | None:
    """Returns superhero from the given index"""
    villains = getAllVillains()
    if index < len(villains):
        return villains[index]
    else:
        return None


# -------------------------- Main logic --------------------------------
def attack() -> None:
    # Attack
    for attackNum in range(3):
        # Each iteration get a new Hero and Villain
        heroIndex = randint(0, 3)
        villainIndex = randint(0, 2)
        # Helper varialbes
        currentSuperHero = getSuperhero(heroIndex)
        currentVillain = getVillain(villainIndex)
        # print(currentSuperHero)
        # print(currentVillain)

        if currentSuperHero and currentVillain:
            simulateAttack(attackNum, currentSuperHero, currentVillain)
        else:
            print("No Superhero or villain to fight")


def simulateAttack(attackNum: int, superhero: Character, villain: Character) -> None:
    """Simulate the actual attack"""

    # Set Life
    incHeroLife(superhero["life"])
    incVillainLife(villain["life"])

    print(
        f"Attack: {attackNum + 1} => {superhero['name']} is going to fight with {villain['name']}"
    )

    # Actual Attack
    decHeroLife(superhero["attackPower"])
    decVillainLife(villain["attackPower"])


# -------------------------- Main logic --------------------------------
def winOrLoose() -> None:
    """Determine if Avenger won or lost"""
    WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

    # Print a nice separating line
    print("=" * 58)
    print(heroLife, villainLife)

    # Win or loose
    if heroLife >= villainLife:
        print(WIN_MSG)
    else:
        print(LOST_MSG)


# -------------------------- Main Function --------------------------------


def main() -> None:
    """Start the Game"""
    attack()
    winOrLoose()


main()
