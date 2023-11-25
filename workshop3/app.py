from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
database = {"admin": "password123"}
donations = []
total = [0]
authorized_user = ""
while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    choice = input("Choose an option: ")
    if choice == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
            # print(database)
    elif choice == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation_string = donate(authorized_user, total)
            if donation_string != "":
                donations.append(donation_string)
    elif choice == "4":
        show_donations(donations, total)
    elif choice == "5":
        print("\n\nLeaving DonateMe...")
        break
    else:
        print("\nPlease enter a valid option.")
    print()
