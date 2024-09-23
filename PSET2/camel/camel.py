def main():

    # Prompts the user for camel case
    camel_case = input("camelCase: ")
    snake_case = convert(camel_case)
    print(snake_case)


def convert(phrase):

    for c in phrase:
        # Checks if character is uppercase
        if c.isupper():
            # Converts camel case to snake case
            phrase = phrase.replace(c, "_" + c.lower())

    return phrase


main()
