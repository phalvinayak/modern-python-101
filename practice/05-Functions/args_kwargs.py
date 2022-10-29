"""
Variable & Keyword Arguments:
-----------------------------

What happens if we don't know before hand how many arguments we are
going to receive? We can handle this situation by using variable &
keyword arguments syntax.

Info:
-----
We will first look at unpacking first.
"""
# -------------------------- Unpacking --------------------------------

from typing import Any

fname, lname = ("Louis", "Zappa")
print(fname, lname)

first, *res = ["Cece", "Roko", "Chiko", "Niko"]
print(first)
print(res)

specs: dict[str, str] = {
    "type": "dynamic",
    "optional": "static typing",
    "found": "everywhere",
}
lang: dict[str, str] = {"name": "python", **specs}
print(lang)


# -------------------------- Variable Arguments --------------------------------


def unknownFriends(*args: str) -> None:
    for friend in args:
        print(friend)


unknownFriends("Cece", "Roko", "Ziko", "Niko", "Chiko")


# -------------------------- Keyword Arguments --------------------------------


def unknownProducts(**kwargs: Any) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")


unknownProducts(name="Pizza", price=3.99, toppings="Olive", extraCheese=True)


# -------------------------- Keyword Arguments --------------------------------


def invoice(product: str, *args: Any, **kwargs: Any) -> None:
    print(product)
    print(args)
    print(kwargs)


invoice(
    "Sneakers",
    "black",
    "white",
    brand="Nike",
    category="Air Jorden",
    price=3.99,
    available=True,
)
