"""
Variable Scope:
---------------

Scopes can be `Global` or `Local`
"""

num = 10


def printGlobalNum() -> None:
    print(f"Global number is: {num}")


def printNum() -> None:
    num = 20
    print(f"Local number is: {num}")


def incNum() -> None:
    # Explicit global declaration
    global num
    num += 2


def incLocalNum() -> None:
    newNum = num + 10
    print(newNum)


printGlobalNum()
printNum()
incNum()
print(num)
incLocalNum()
