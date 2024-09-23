import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):
        groups = match.groups()
        if int(groups[1]) > 12 or int(groups[5]) > 12:
            raise ValueError
        f_time = format_convert(groups[1], groups[2], groups[3])
        s_time = format_convert(groups[5], groups[6], groups[7])
        return f"{f_time} to {s_time}"
    else:
        raise ValueError

def format_convert(h, m, am_pm):
    if am_pm == "PM":
        if int(h) == 12:
            new_h = 12
        else:
            new_h = int(h) + 12
    else:
        if int(h) == 12:
            new_h = 0
        else:
            new_h = int(h)
    if m == None:
        new_m = ":00"
        new_time = f"{new_h:02}{new_m}"
    else:
        new_time = f"{new_h:02}:{m}"
    return new_time

if __name__ == "__main__":
    main()
