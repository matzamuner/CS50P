def main():
    # Prompts the value of "m" from the user
    m = int(input("m: "))
    e = energy(m)
    # Prints calculated energy
    print(e)


def energy(m):
    # Calculates energy
    c = 300000000
    e = m * c**2
    return e


main()
