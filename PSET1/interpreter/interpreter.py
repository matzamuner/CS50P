def main():
    # Prompts the user for input
    x, y, z = input("Expression: ").split()
    # Interprets function
    result = interpreter(float(x), y, float(z))
    # Prints result
    print(f"{result:.1f}")


def interpreter(x, y, z):
    # Matches each operator
    match y:
        case "+":
            return (x + z)
        case "-":
            return (x - z)
        case "*":
            return (x * z)
        case "/":
            return (x / z)


main()
