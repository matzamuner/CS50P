def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Prompts the user for a date in month-day-year order
    while True:
        # Checks for correct date input
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.split()
            if month in months:
                month = months.index(month)
                month += 1
                day = day.strip(",")
        else:
            continue
        try:
            if int(day) > 31 or int(month) > 12:
                continue
            else:
                break
        except ValueError:
            continue
    # Prints formatted date
    print(f"{year}-{int(month):02}-{int(day):02}")


main()
