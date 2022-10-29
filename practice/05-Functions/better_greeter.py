"""
Functions:
----------
Think in data transformations -
`take something -> give something`

Delegate handling responsibility to the caller function.

Tip:
-----
Very useful pattern for testing!!!
"""


def greeter(name: str) -> str:
    """Returns a Greeting message in Zortan"""
    # Returns `transforms` original string to something useful
    # and returns it.
    return f"Zola {name}"


def main() -> None:
    friends: list[str] = ["Cece", "Roko", "Chiko", "Niko", "Ziko"]
    for friend in friends:
        # Main acts as the caller function for greeter
        # it can handle response in multiple ways
        greetMsg: str = greeter(friend)
        if "Chiko" in greetMsg:
            print(f"{friend} is cute!")
        else:
            print(greetMsg)


# Invoke our `main` function
main()
