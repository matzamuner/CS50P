def main():
    # Prompts the user for input
    greeting = input("Greeting: ").strip().lower()
    # Calculates amount
    amount = value(greeting)
    # Prints amount
    print(f"${amount}")


def value(greeting):
    # Splits greeting
    greeting = greeting.split()
    # Checks if "hello" or "h" in greeting
    if "hello" in greeting[0]:
        return "0"
    elif "h" in greeting[0][0]:
        return "20"
    else:
        return "100"


main()
