from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
# Error checking
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid argument number")
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid argument")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid argument font")
# Prompts the user for input
s = input("Input: ")
# Sets font
if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

print(figlet.renderText(s))
