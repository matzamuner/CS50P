def main():
    fraction = input("Fraction: ")
    fraction = convert(fraction)
    print(gauge(fraction))


def convert(fraction):
    fraction = fraction.split("/")
    if int(fraction[1]) == 0:
        raise ZeroDivisionError
    elif int(fraction[0]) > int(fraction[1]):
        raise ValueError
    return (int(fraction[0]) / int(fraction[1]) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"



if __name__ == "__main__":
    main()
