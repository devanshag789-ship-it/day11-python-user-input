# input() returns text (str); float() supports integers and decimals.

def get_number(prompt):
    """Read a number from the user, retrying if the input is invalid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a numeric value (e.g. 12 or 3.5).")


name = input("Enter a name: ").strip()

print("The name is", name)
print("This is a user input program")

x = get_number("Enter your first number: ")
y = get_number("Enter your second number: ")

print("The type of x is", type(x))
print("The type of y is", type(y))

print("Sum =", x + y)
