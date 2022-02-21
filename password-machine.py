input("WELCOME TO PASSWORD MACHINE press enter to continue")
while True:
    password = input("Enter the password:")
    if password == "Daddyisbest" or password == "6547":
        print("System online")
        break
    elif int(password) < 6547:
        print("Your password is too low!")
    else:
        print("Your password is too high!")
