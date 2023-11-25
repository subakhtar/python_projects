class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name + " has an account balance of: $" + str(self.balance))

    def withdraw(self, amount):
        if str(amount).isdecimal > self.balance:
            print("Account balance is too low for this withdrawal amount")
            return
        if amount > self.balance:
            print("Account balance is too low for this withdrawal amount")
            return
        if amount > self.balance:
            print("Account balance is too low for this withdrawal amount")
            return
        self.balance -= amount
        # self.show_balance()

    def deposit(self, amount):
        self.balance += amount
        # self.show_balance()

    def transfer_money(self, BankUser, amount):
        print("\nYou are transferring $" + str(amount) + " to " + BankUser.name)
        pinNum = input("Authentication required\nEnter your PIN: ")
        if str(pinNum) == str(self.pin):
            if self.balance < amount:
                print("Insufficient funds for transfer. Transaction canceled.")
                return False
            else:
                print("Transfer authorized\nTransferring $" + str(amount) + " to " + BankUser.name)
                self.balance -= amount
                BankUser.balance += amount
                return True
        else:
            print("Invalid PIN. Transaction canceled.")
            return False

    def request_money(self, BankUser, amount):
        print("\nYou are requesting $" + str(amount) + " from " + BankUser.name)
        pinNum = input("User authentication is required...\nEnter " + BankUser.name + "'s PIN: ")
        if str(pinNum) == str(BankUser.pin):
            pwd = input("Enter your password: ")
            if str(pwd) == str(self.password):
                if BankUser.balance < amount:
                    print("Insufficient funds for transfer. Transaction canceled.")
                    return False
                else:
                    print("Request authorized\n" + BankUser.name + " sent $" + str(amount))
                    BankUser.balance -= amount
                    self.balance += amount
                    return True
            else:
                print("Invalid password. Transaction canceled.")
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            return False


""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 2 """
# user2 = User("Bob", 1234, "password")
# print(user2.name, user2.pin, user2.password)
# user2.change_name("Bobby")
# user2.change_pin(4321)
# user2.change_password("newpassword")
# print(user2.name, user2.pin, user2.password)

""" Driver Code for Task 3 """
# user1 = BankUser("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password, user1.balance)

""" Driver Code for Task 4"""
# user1 = BankUser("Bob", 1234, "password")
# user1.show_balance()
# user1.deposit(1000.0)
# user1.show_balance()
# user1.withdraw(500)
# user1.show_balance()

""" Driver Code for Task 5"""
user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Alice", 2222, "pwd")
sent = False
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
sent = user2.transfer_money(user1, 500.0)
user2.show_balance()
user1.show_balance()
if sent:
    user2.request_money(user1, 250)
    user2.show_balance()
    user1.show_balance()
