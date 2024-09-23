import random


def main():
    level = get_level()
    score = 0
    # Starts little professor game and prints final score
    for i in range(10):
        x = int(generate_integer(level))
        y = int(generate_integer(level))
        for j in range(3):
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                score += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print(f"{x} + {y} = {x+y}")
    print("Score:", score)


def get_level():
    # Prompts the user for input on level
    while True:
        level = input("Level: ")
        try:
            level = int(level)
        except ValueError:
            continue
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue


def generate_integer(level):
    # Generates random integer based on level
    match level:
        case 1:
            x = random.choice(range(10))
            return x
        case 2:
            x = random.choice(range(10, 99))
            return x
        case 3:
            x = random.choice(range(100, 999))
            return x

if __name__ == "__main__":
    main()
