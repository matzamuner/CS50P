import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
