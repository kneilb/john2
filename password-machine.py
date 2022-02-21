import random
password = random.randint(1, 10000)

input("WELCOME TO PASSWORD MACHINE press enter to continue")

while True:
    guess = input("Enter the password:")
    guess = int(guess)
    if guess == password:
        print("System online")
        break
    elif guess < password:
        print("Your password is too low!")
    else:
        print("Your password is too high!")
