def main():
    # Prompts the user
    time = input("What time is it? ")
    # Converts inputed time
    time = convert(time)
    # Prints corresponding meal
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    return float(hours) + minutes


if __name__ == "__main__":
    main()
