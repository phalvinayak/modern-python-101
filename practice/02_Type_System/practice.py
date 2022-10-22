"""
Louis wants to open a Pizza Shop and needs to write
a program for accepting orders.

Tip - 1
-------
First Visualize First, then start coding
"""

customer: str = "Cece"
pizzaBase: str = "Thin"
pizzaSize: int = 12
toppings: str = "Olives"
extraCheese: bool = True
price: float = 8.99

# -----------------------------------------
# Alternative 1 - Using print functions
# -----------------------------------------
print(f"Received order from: {customer}")
print(f"Pizza base: {pizzaBase}, Size: {pizzaSize} Inches, Toppings: {toppings}")
print(f"Is Extra Cheese required: {extraCheese}")
print(f"Bill Amount: {price}")

# -----------------------------------------
# Alternative 2 - Using Formatted string
# -----------------------------------------
orderDetails: str = f"""
Received order from: {customer}
Pizza base: {pizzaBase}, Size: {pizzaSize} Inches, Toppings: {toppings}
Is Extra Cheese required: {extraCheese}
Bill Amount: {price}
"""

print(orderDetails)

# -----------------------------------------
# Alternative 3 - Using Formatted string
# -----------------------------------------
print(
    f"""
Received order from: {customer}
Pizza base: {pizzaBase}, Size: {pizzaSize} Inches, Toppings: {toppings}
Is Extra Cheese required: {extraCheese}
Bill Amount: {price}
"""
)
