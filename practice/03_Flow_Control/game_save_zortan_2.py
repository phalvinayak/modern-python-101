"""
Zortan is under attack!!! Thanos has arrived!
---------------------------------------------

Since Zortan is under attack, Louis calls his Avenger friends from earth.
Avengers receive his call and sends 4 avengers to save Zortan.

1. Ironman
4. Black Widow
2. Spiderman
3. Hulk

Each avenger has its attacking power and they have to fight Thanos
to save Zortan.

Avengers can attack only in pairs and get only 3 chances to kill Thanos,
or else Thanos will kill avengers and we loose the game.
"""

from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanosLife: int = 1500
choice: int = 0
attackNumber: int = 0

# declare helper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!! ✨ ✨ ✨"
LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!! 💀 💀 💀"
MSG: Final[
    str
] = """
---------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will attack Thanos

1) Ironman
2) Black Widow
3) Spiderman
4) Hulk
---------------------------------------------------------------------
"""

while True:

    # Break out on Win / Loose
    if thanosLife <= 0 and attackNumber <= 3:
        print(WIN_MSG)
        break
    elif attackNumber >= 3:
        print(LOST_MSG)
        break

    print(MSG)
    print("Enter your super hero pair by entering numbers of it")
    choice1 = int(input(" Enter your 1st Superhero >>> "))
    choice2 = int(input(" Enter your 2nd Superhero >>> "))

    attackNumber = attackNumber + 1
    superHero1: str = ""
    superHero2: str = ""

    if choice1 == choice2:
        print("You cannot choose same super hero, you lost a chance.")

    match choice1:
        case 1:
            thanosLife = thanosLife - IRONMAN_ATTACK_POWER
            superHero1 = "IronMan"
        case 2:
            thanosLife = thanosLife - BLACKWIDOW_ATTACK_POWER
            superHero1 = "Black Widow"
        case 3:
            thanosLife = thanosLife - SPIDERMAN_ATTACK_POWER
            superHero1 = "Spiderman"
        case 4:
            thanosLife = thanosLife - HULK_ATTACK_POWER
            superHero1 = "Hulk"
        case _:
            thanosLife = thanosLife - 0
            superHero1 = "unkonwn"

    match choice2:
        case 1:
            thanosLife = thanosLife - IRONMAN_ATTACK_POWER
            superHero2 = "IronMan"
        case 2:
            thanosLife = thanosLife - BLACKWIDOW_ATTACK_POWER
            superHero2 = "Black Widow"
        case 3:
            thanosLife = thanosLife - SPIDERMAN_ATTACK_POWER
            superHero2 = "Spiderman"
        case 4:
            thanosLife = thanosLife - HULK_ATTACK_POWER
            superHero2 = "Hulk"
        case _:
            thanosLife = thanosLife - 0
            superHero2 = "unkonwn"

    print(f"{superHero1} and {superHero2} are attacking Thanos!!")
