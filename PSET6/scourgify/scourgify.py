import sys
import csv

# Checks if command-line is correct
if len(sys.argv) != 3:
    sys.exit("Invalid argument number")
elif ".csv" not in sys.argv[1]:
    sys.exit("Invalid file format")

with open(sys.argv[1]) as before, open(sys.argv[2], "w") as after:
    reader = csv.DictReader(before)
    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
    writer.writeheader()
    # Iterates through row in before.csv
    for row in reader:
        last, first = row["name"].split(", ")
        writer.writerow(
            {
                "first": first,
                "last": last,
                "house": row["house"]
            }
        )
