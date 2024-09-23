def main():
    # Prompts input from the user
    phrase = input("Enter a phrase: ")
    phrase = convert(phrase)
    # Prints new phrase
    print(phrase)

# Converts the emoticons to emoji


def convert(phrase):
    # Replaces any emoticons
    phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
    # Returns new phrase
    return phrase


main()
