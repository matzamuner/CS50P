def main():
    # Prompts the user the question
    answer = question()
    # Prints answer
    print(answer)


def question():
    # Prompts user
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    # Matches the user inputed answer
    match answer:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"


main()
