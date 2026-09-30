# validation.py
# Functions that check what the user types, so the program does not crash


def is_valid_name(name):
    # name should not be empty and should have only letters and spaces
    name = name.strip()
    if name == "":
        return False
    return name.replace(" ", "").isalpha()


def is_valid_quantity(quantity):
    # we allow 1 to 50 items of one kind
    return 1 <= quantity <= 50


def get_number(message, minimum, maximum):
    # keeps asking until the user enters a whole number in the range
    while True:
        text = input(message)
        try:
            number = int(text)
        except ValueError:
            print("Please enter a number only.")
            continue

        if number < minimum or number > maximum:
            print("Number must be between", minimum, "and", maximum)
        else:
            return number


def get_name(message):
    # keeps asking until the user enters a proper name
    while True:
        name = input(message)
        if is_valid_name(name):
            return name.strip()
        print("Name cannot be empty and must have only letters.")
