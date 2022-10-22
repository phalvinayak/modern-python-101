"""
While traveling to Zortan, Louis packed lots of stuff. Let's
see if he has anything that matches your favorite color.

INFO -
------

`match` is a new operator introduced in Python 3.10
"""

favColor = input("Enter your favourite color: ")
print(favColor)

match favColor.lower():
    case "black":
        print("Louis has a Black T-Shirt")
    case "red":
        print("Louis has a Red Car")
    case "yellow":
        print("Louis has a Yellow Shoes")
    case "green":
        print("Louis has a Green Hat")
    case _:
        print(f"Louis has nothing in {favColor} color")
