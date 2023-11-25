def show_homepage():
    print("       === DonateMe Homepage ===")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")


def donate(username, total):
    donation_amt = input("\nEnter amount to donate: ")
    if str.isdecimal(donation_amt) and float(donation_amt) > 0:
        amt = float(donation_amt)
        total[0] += amt
        donation_string = username + " donated $" + str(amt)
        # print(donation_string)
        print("Thank you for your donation!")
        return donation_string
    elif len(donation_amt) > 3:
        if donation_amt[-3] == ".":
            if str.isdecimal(donation_amt[0:-3]) and str.isdecimal(donation_amt[-2:-1]):
                amt = float(donation_amt)
                total[0] += amt
                donation_string = username + " donated $" + str(amt)
                # print(donation_string)
                print("Thank you for your donation!")
                return donation_string
    elif len(donation_amt) == 3:
        if donation_amt[-3] == ".":
            if str.isdecimal(donation_amt[-2:-1]):
                amt = float(donation_amt)
                total[0] += amt
                donation_string = username + " donated $" + str(amt)
                # print(donation_string)
                print("Thank you for your donation!")
                return donation_string
    print("Donation amount must be a real number greater than 0")
    return ""


def show_donations(donations, total):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
        print("Total = $" + str(total[0]))
