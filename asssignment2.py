import datetime

currentBalance = 0
balance_changes = []


def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%H:%M %d/%m/%Y")


def add_amount():
    global currentBalance
    amount = int(input("Enter the amount to deposit in your bank account : "))
    currentBalance += amount
    balance_changes.append(
        f"At {get_timestamp()}: Add ${amount} to the current balance\n")
    return


def subtract_amount():
    global currentBalance
    amount = int(
        input("Enter the amount to withdraw from your bank account : "))
    if currentBalance >= amount:
        currentBalance -= amount
        balance_changes.append(
            f"At {get_timestamp()}: Withdraw ${amount} from the current balance\n")
    else:
        print(
            f"The amount exceeds your current balance by ${amount - currentBalance}")
        balance_changes.append(
            f"At {get_timestamp()}: Failed attempt to withdraw ${amount} due to insufficient bank balance\n")
    return


def get_balance():
    global currentBalance
    print(f"Your bank account's current balance : ${currentBalance}")
    return


def view_balance_changes():
    global balance_changes
    for change in balance_changes:
        print(change)


def main(choice):
    if choice == 'A':
        add_amount()
    elif choice == 'S':
        subtract_amount()
    elif choice == 'G':
        get_balance()
    elif choice == 'H':
        view_balance_changes()


choice = ""

while choice != "Q":
    choice = input(
        """
    choose one of the follow choice :
    A - Add an amount of money to your bank account
    S - Subtract an amount of money from your bank account
    G - Get the balance of your bank account
    H - View history of changes of the bank balance
    Q - Quit
    """
    ).upper()
    main(choice)
