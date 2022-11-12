"""
Save Zortan:
------------

Let's improve our design by using classes.

"""

# import the stuff we require
from random import randint
from typing import Final
from enum import Enum, auto


class CharacterType(Enum):
    SUPER_HERO = auto()
    VILLAIN = auto()


class Character:
    def __init__(self, name: str, attackPower: int, life: int) -> None:
        self.name = name
        self.attackPower = attackPower
        self.life = life

    def __str__(self) -> str:
        return f"Name: {self.name}, Attack Power: {self.attackPower}, Life: {self.life}"


class SuperHero(Character):
    def __init__(self, name: str, attackPower: int, life: int) -> None:
        super().__init__(name, attackPower, life)
        self.role = CharacterType.SUPER_HERO

    def __str__(self) -> str:
        return f"SuperHero: {super().__str__()}"


class Villain(Character):
    def __init__(self, name: str, attackPower: int, life: int) -> None:
        super().__init__(name, attackPower, life)
        self.role = CharacterType.VILLAIN

    def __str__(self) -> str:
        return f"Villain: {super().__str__()}"


# --------------------- LIFE -----------------------------
class Life:
    """
    Helper class for managing Life.

    NOTE: Also see `Data Classes` for alternative solution.
    url - https://docs.python.org/3/library/dataclasses.html
    """

    heroLife: int = 0
    villainLife: int = 0

    @staticmethod
    def incHeroLife(life: int) -> None:
        """Increment hero life"""
        Life.heroLife += life

    @staticmethod
    def incVillainLife(life: int) -> None:
        """Increment villain life"""
        Life.villainLife += life

    @staticmethod
    def decHeroLife(life: int) -> None:
        """Decrement hero life"""
        Life.heroLife -= life

    @staticmethod
    def decVillainLife(life: int) -> None:
        """Decrement hero life"""
        Life.villainLife -= life


# -------------------------- Superheroes --------------------------------
def getAllSuperheros() -> list[SuperHero]:
    # Super Heroes
    ironMan = SuperHero("IronMan", 250, 1000)
    blackWidow = SuperHero("IronMan", 180, 800)
    spiderMan = SuperHero("IronMan", 190, 750)
    hulk = SuperHero("IronMan", 300, 1000)

    superheroes: list[SuperHero] = [ironMan, blackWidow, spiderMan, hulk]
    return superheroes


def getSuperhero(index: int) -> SuperHero | None:
    """Returns superhero from the given index"""
    superheroes = getAllSuperheros()
    if index < len(superheroes):
        return superheroes[index]
    else:
        return None


# -------------------------- Villains --------------------------------
def getAllVillains() -> list[Villain]:
    # Super Villains
    thanos = Villain("Thanos", 400, 1500)
    redskull = Villain("Redskull", 300, 800)
    proxima = Villain("Proxima", 320, 800)

    villains: list[Villain] = [thanos, redskull, proxima]
    return villains


def getVillain(index: int) -> Villain | None:
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


def simulateAttack(attackNum: int, superhero: SuperHero, villain: Villain) -> None:
    """Simulate the actual attack"""

    # Set Life
    Life.incHeroLife(superhero.life)
    Life.incVillainLife(villain.life)

    print(
        f"Attack: {attackNum + 1} => {superhero.name} is going to fight with {villain.name}"
    )

    # Actual Attack
    Life.decHeroLife(villain.attackPower)
    Life.decVillainLife(superhero.attackPower)


# -------------------------- Main logic --------------------------------
def winOrLoose() -> None:
    """Determine if Avenger won or lost"""
    WIN_MSG: Final[str] = "Avengers successfully saved Zortan!!! ✨ ✨ ✨"
    LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"

    # Print a nice separating line
    print("=" * 58)
    print(Life.heroLife, Life.villainLife)

    # Win or loose
    if Life.heroLife >= Life.villainLife:
        print(WIN_MSG)
    else:
        print(LOST_MSG)


# -------------------------- Main Function --------------------------------


def main() -> None:
    """Start the Game"""
    attack()
    winOrLoose()


main()
