def login(database, username, password):
    for name in database:
        if str.lower(name) == str.lower(username):
            if database[name] == password:
                print("\nWelcome back", name + "!")
                return name
            else:
                print("\nIncorrect password for", name)
                return ""
    else:
        print("\nUser not found. Please register.")
        return ""
    return ""


def register(database, username, password):
    for name in database:
        if str.lower(name) == str.lower(username):
            print("\nUsername already registered")
            return ""
    if len(username) <= 10 and len(password) >= 5 and username != "":
        if username[0].isalpha():
            print("Username", username, "registered!")
            return username
    if len(username) > 10:
        print("Username must not exceed 10 characters")
    if len(password) < 5:
        print("Password must be greater than 5 characters")
    if username != "":
        if username[0].isdigit():
            print("Username must begin with a letter")
    return ""
