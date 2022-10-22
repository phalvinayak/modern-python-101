"""
Louis wants to drive a car and he hears that in planet
Zortan there in no age limit for getting a license.
"""

age: int = 13
planet: str = "Earth"

# ------------------------------------
# And / Or Statement
# ------------------------------------

if age < 16 and planet == "Earth":
    print("You're not eligible for a license on Earth")
elif age > 16 and planet == "Earth":
    print("You can apply for a license on Earth")
elif age < 16 or planet == "Zortan":
    print("You can apply for a Zortanian license!!")


# ------------------------------------
# Louis moves to Zortan
# ------------------------------------

planet = "Zortan"

if age < 16 and planet == "Earth":
    print("You're not eligible for a license on Earth")
elif age > 16 and planet == "Earth":
    print("You can apply for a license on Earth")
elif age < 16 or planet == "Zortan":
    print("You can apply for a Zortanian license!!")
