def main():
    # Prompts the user for a vanity plate
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Checks if it is a valid vanity plate
    if 6 >= len(s) >= 2 and s.isalnum() and s[0:2].isalpha():
        # Iterates through all characters in vanity plate
        for c in s:
            if c.isdigit():
                i = s.index(c)
                if s[i:].isdigit() and c != "0":
                    return True
                else:
                    return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
