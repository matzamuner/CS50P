import random

# Prompts the user for the level
while True:
    n = input("Level: ")
    try:
        n = int(n)
    except ValueError:
        continue
    else:
        if n <= 0:
            continue
        else:
            break
# Chooses a random number between 0 and n
x = random.choice(range(0, n))
# Prompts the user for a guess
while True:
    g = input("Guess: ")
    try:
        g = int(g)
    except ValueError:
        continue
    else:
        if g <= 0:
            continue
        else:
            if g < x:
                print("Too small!")
            elif g > x:
                print("Too large!")
            else:
                print("Just right!")
                break
