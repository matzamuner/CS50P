def main():
    # Prompts for fuel
    n = fuel()
    # Prints corresponding fuel
    if n >= 99:
        print("F")
    elif n <= 1:
        print("E")
    else:
        print(f"{n:.0f}%")


def fuel():
    # Calculates fuel percentage
    while True:
        try:
            x = input("Fraction: ").split("/")
            y = (int(x[0]) / int(x[1]) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if y > 100:
                continue
            else:
                return y


main()
