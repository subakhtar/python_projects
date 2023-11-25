def show_balance(balance):
    print("Current balance: $" + str(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    total = float(amount) + balance
    return total


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if float(amount) > balance:
        print("Where are you going to get that kind of money from?")
        return balance
    else:
        total = balance - float(amount)
        return total


def logout(name):
    print("Goodbye", name + "!")
