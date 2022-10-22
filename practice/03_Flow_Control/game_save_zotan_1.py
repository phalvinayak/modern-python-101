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

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
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
    choice = int(input(" Enter your pair number >>> "))

    if choice == 1:
        print("Ironman and Black Widow are attacking Thanos")
        thanosLife = thanosLife - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attackNumber = attackNumber + 1
    elif choice == 2:
        print("Black Widow and Spiderman are attacking Thanos")
        thanosLife = thanosLife - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attackNumber = attackNumber + 1
    elif choice == 3:
        print("Spiderman and Hulk are attacking Thanos")
        thanosLife = thanosLife - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attackNumber = attackNumber + 1
    elif choice == 4:
        print("Hulk and Ironman are attacking Thanos")
        thanosLife = thanosLife - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attackNumber = attackNumber + 1
