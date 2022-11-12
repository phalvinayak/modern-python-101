"""
Class can have class variables as well as instance variables.

Class variables are shared across all instances while instance
variable are only limited to that particular instance.
"""

class Box:
    # Classs Varialbes/Member
    boxType = "Packaging Carton"
    color = "Brown"

    def __init__(self, sideA: int, sideB: int) -> None:
        self.sideA = sideA
        self.sideB = sideB
        
    def __str__(self) -> str:
        return f"Side A: {self.sideA}, Side B: {self.sideB}"

b1 = Box(3, 4)
print(b1)

print(b1.boxType)
print(b1.color)

print(Box.boxType)
print(Box.color)

b2 = Box(7, 8)
print(b2)
print(b2.boxType)
print(b2.color)