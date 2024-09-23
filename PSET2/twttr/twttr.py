def main():

    # Prompts the user for a phrase/word
    phrase = input("Input: ")
    phrase = convert(phrase)
    print(f"Output: {phrase}")


def convert(string):

    # Converts vowels
    for c in string:
        match c.lower():
            case "a" | "e" | "i" | "o" | "u":
                print(c)
                string = string.replace(c, "")

    # Returns converted string
    return string


main()
