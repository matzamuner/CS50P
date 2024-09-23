import inflect

p = inflect.engine()
names = []
# Prompts the user for input until ctrl-d is pressed
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print("")
        break
# Formats names
s = p.join((names[0:]))
# Print names
print("Adieu, adieu, to", s)
