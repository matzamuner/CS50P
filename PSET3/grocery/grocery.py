def main():
    # Grocery list dictionary
    grocery_list = {}
    # Prompts the user for input until ctrl-d is pressed
    while True:
        try:
            item = input().upper()
        except EOFError:
            print("")
            break
        else:
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
    # Iterates through the grocery_list dict in alphabetical order
    keys = sorted(grocery_list)
    values = grocery_list.values()
    for i in range(len(keys)):
        print(list(values)[i], keys[i])


main()
