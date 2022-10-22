"""
Friend from earth want to know where Louis, so Louis decides to
write a program that will make his friends guess the name of the planet.
"""

correctGuess: bool = False
guess: str = ""
planet: str = "Zortan"

# ---------------------------------
# Alternative - 1
# ---------------------------------

# while correctGuess is not True:
#     guess = input("Louis Says: Can you guess my planet? >>> ")
#     if planet.lower() == guess.lower():
#         correctGuess = True
#         print("Correct Guess!! Louis is at Zortan")
#     else:
#         print(f"Louis Says: Wrong guess {guess}, Try again")


# ---------------------------------
# Alternative - 2
# ---------------------------------

while True:
    guess = input("Louis Says: Can you guess my planet? >>> ")
    if planet.lower() == guess.lower():
        print("Correct Guess!! Louis is at Zortan")
        break
    else:
        print(f"Louis Says: Wrong guess {guess}, Try again")
