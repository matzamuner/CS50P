def main():

    # Coke price
    amount_due = 50

    while True:

        # Checks if the price has been paid and the change owed
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")
            break

        # Prompts the user for coin amount
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))

        match coin:
            case 25:
                amount_due = amount_due - 25
            case 10:
                amount_due = amount_due - 10
            case 5:
                amount_due = amount_due - 5


main()
