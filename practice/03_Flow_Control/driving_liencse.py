"""
Loius wants to drive a car and wants to know if he can
apply for a driving license or not
"""

age: int = 13

# ---------------------------------------------------
# If / Else / Elif Statement
# ---------------------------------------------------

if age < 16:
    print("You are NOT eligilble for License")
else:
    print("You are eligigle for License")

# ---------------------------------------------------
# Few Years later
# ---------------------------------------------------

age = 100

if age < 16:
    print("You are NOT eligilble for License.")
elif age >= 100:
    print("You're too old for the diving license.")
else:
    print("You are eligigle for License.")
