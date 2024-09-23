def main():
    # Prompts the user for input on the meal
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    # Prints calculated tip
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Removes dollar sign from string
    d = d.strip("$")
    # Returns d as a float
    return float(d)


def percent_to_float(p):
    # Removes percent sign from string
    p = p.strip("%")
    p = float(p)
    # Returns p as a float
    return p / 100


main()
