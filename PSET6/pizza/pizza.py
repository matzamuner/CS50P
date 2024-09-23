from tabulate import tabulate
import csv
import sys
# Checks if command-line is correct
if len(sys.argv) != 2:
    sys.exit("Invalid argument number")
elif ".csv" not in sys.argv[1]:
    sys.exit("Invalid file format")
# Opens csv file and tabulates it
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exit")
