def main():
    # Taqueria dictionary
    taqueria = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    value = 0
    while True:
        try:
            # Prompts the user for input on order
            order = input("Item: ").title()
            if order in taqueria:
                value += taqueria[order]
        except EOFError:
            print("")
            break
        else:
            # Prints the total value of order
            print(f"Total: ${value:.2f}")


main()
