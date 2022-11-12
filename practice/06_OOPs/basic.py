"""
Class:
------
`Class` are just like a building blueprint, they provide you with the
specifications of how to construct a building. It is upto you when and
how you build the building.

Instance:
---------
When you actually construct a building out of the blueprint, it is called as
an `Instance` or `Object` of the class. So, both are related but essential
different terminology.

Class = Blueprint, Instance = Building

Methods:
--------
These are just normal functions, but defined to alter the behavior of your instance or class.
Since they are tied to a class, they are called as methods. Their behavior is dependent on
the structure you define in the class.

When to use Class:
------------------
Use classes only when you need `Structure` and `Behavior` together.

If you only need structure, then choose from any existing data structures such as
list, tuple, dictionary, queue, etc. Just need a behavior? Then just create a function
that transforms your data.

"""
# -------------------------------------------------------------------------

class SomeClass:
    """Defines an empty class"""
    pass

print(SomeClass)

# -------------------------------------------------------------------------

class Person:
    """Defines a Person"""

    def __init__(self, firstName: str, lastName: str) -> None:
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self) -> str:
        return '<class "Person">'

    def __str__(self) -> str:
        """This magic method provides string representation of an instace"""
        return f"Person: {self.firstName} {self.lastName}"

    def greet(self) -> None:
        """This is a function that prints greeting message"""
        print(f"{self.firstName} says Hello!")

p1 = Person("Louis", "Zappa")
p2 = Person("Cece", "Neutron")
print(p1)
print(p2)

print(p1.firstName)
print(p2.firstName)

# Both are different instances of the same class at different memory location
print(f"p1 is located a memory address: {hex(id(p1))}")
print(f"p2 is located a memory address: {hex(id(p2))}")

# Possible but not recommended
print(p1.__str__())

# Calling methods on a perticular object
p1.greet()
p2.greet()