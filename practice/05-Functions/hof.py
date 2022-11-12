"""
Higher Order Functions:
-----------------------
Please note that this is a advanced topic, so it may take a couple of attempts
to understand these concepts.

Functions under the hood are just `Objects`, they can be passed to other
functions and functions can also return functions!

This data type is called as `Callable`, one which can be called or invoked.

Note:
-----
Till now we have been sending data to our functions, but sending data every time
can be expensive, instead we can send function to data!

Don't spend too much time mastering this topic, it will come naturally as you
progress with your programming skills.
"""
# -------------------------------------------------------------------------

from typing import Callable

def hello() -> None:
    """Prints Hello World!"""
    print("Hello World!")


# Hello is just a regular object of class of type `function`
print(hello)
print(id(hello))
print(hex(id(hello)))

# We can assign function to variables
greet: Callable[[], None] = hello # Just assigning the object Hello
greet() # We can invoke/call the function using `()` at the end
#-----------------------------------------------------------------------

"""
Let's try to create a universal greeter that can greet a person in multiple
ways.
"""

def zola(name: str) -> str:
    return f"Zola, {name}"

def goodMorning(name: str) -> str:
    return f"Good Morning, {name}"

def goodbye(name: str) -> str:
    return f"Goodbye, {name}"

# Function accepting a function
def universalGreeter(name: str, greeter: Callable[[str], str]) -> None:
    msg = greeter(name)
    print(msg)

universalGreeter("Louis", zola)
universalGreeter("Octallium", goodMorning)
universalGreeter("England", goodbye)

#-----------------------------------------------------------------------

"""
Function reutrning functions!!
------------------------------

This ca be confusing, relax if you can't get it, it took me several 
attempts to understand this!
"""

# Function returning a function
def addBy5(num: int) -> Callable[[], int]:
    """Add by 5"""

    def by5() -> int:
        return num + 5
    
    return by5

sum = addBy5(5)
print(sum())


# Function returning a function
def uniqueAdder(num1: int) -> Callable[[int], int]:
    """Add 2 number and subtracts by 1"""

    def adder(num2: int) -> int:
        return num1 + num2 -1

    return adder

adder = uniqueAdder(5)
print(adder(5))

# ----------------------------------------------------------------------------------------
"""
Lambda:
-------

Perhaps the most neglected, but very powerful technique to work with functions.
Again, don't spend too much time mastering it, it will come naturally!

The way in which we declared functions are very verbose, we can condense them
in a single statement.

Let's try to create a calculator from scratch
"""

add: Callable[[int, int], int] = lambda x, y: x + y
subtract: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], int] = lambda x, y: x * y

def calc(num1: int, num2: int, operation: Callable[[int, int], int]) -> int:
    """Performs the math operations on the numbers"""
    return operation(num1, num2)

print(calc(4, 5, add))
print(calc(4, 5, subtract))
print(calc(4, 5, multiply))
