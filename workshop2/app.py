from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
while str.__len__(name) > 10:
    print("The maximum name length is 10 characters.")
    name = input("Enter name to register: ")
pin = input("Enter PIN: ")
while str.__len__(pin) != 4:
    print("PIN must contain 4 numbers.")
    pin = input("Enter PIN: ")
balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))

while True:
    print("\n          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
while True:
    # print("\n          === Automated Teller Machine ===          ")
    # print("User:", name)
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Please enter a valid menu option.")
