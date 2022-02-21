input("WELCOME TO PASSWORD MACHINE press enter to continue")
while True:
    password = input("Enter the password:")
    if password == "Daddyisbest" or password == "6547":
        print("System online")
    else:
        if int(password) < 6547:
            print("Your password is to low!")
        else:
            print("Your password is to high!")
