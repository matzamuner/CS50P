from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    converted_date = convert(input("Date of Birth: "))
    print(f"{converted_date.capitalize()} minutes")


def convert(s):
    try:
        year, month, day = s.split("-")
        born_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid Date")
    diference = date.today() - born_date
    diference = diference.total_seconds()
    diference = diference / 60
    words = p.number_to_words(f"{diference:.0f}", andword="")
    return words

if __name__ == "__main__":
    main()
