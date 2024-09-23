import sys
# Checks if command-line is correct
if len(sys.argv) != 2:
    sys.exit("Invalid argument number")
elif ".py" not in sys.argv[1]:
    sys.exit("Invalid file format")
lines = 0
# Iterates through file counting lines
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.isspace() or line.lstrip().startswith("# "):
                continue
            else:
                lines += 1
except FileNotFoundError:
    sys.exit("File does not exit")
print(lines)
