import random
import time
password = random.randint(1, 100) #100

# google #
def google():
    print()
    google_search = input("What shall you search? ")
    print(f"Sorry, {google_search} is not valid.")
    exit_google = input("would you like to exit google? y for yes and n for no: ")
    if exit_google == "n":
        google()
    else:
        computer_is_on()

# gmail #
def gmail():
    print()
    contact = input("Please add somebody to your contacts. Add their name here: ")
    gmail_choice1 = input(f"would you like to contact {contact}? y for yes and n for no: ")
    if gmail_choice1 == "y":
        print()
        time.sleep(3)
        print("hello!")
        time.sleep(10)
        print("I am eating currently...")
        time.sleep(10)
        print("Sorry I'll ring you later.")
        time.sleep(3)
        gmail()
    if gmail_choice1 == "n":
        exit_gmail = input("would you like to exit gmail? y for yes and n for no: ")
        if exit_gmail == "n":
            gmail()
        else:
            computer_is_on()

##################
# COMPUTER IS ON #
##################
def computer_is_on():
    time.sleep(2.5)
    print()
    app_chosen = input("Would you like to use: google, gmail, fish catcher, cheese monkey simulator or the app store? ")
    if app_chosen == "google":
        google()
    if app_chosen == "gmail":
        gmail()

# start #
def start():
    guess = input("Enter what you think is the password that is from 0 to 100: ")
    guess = int(guess)
    if guess == password:
        print("System online")
        computer_is_on()
    if guess < password:
        print("Your password is too low!")
        start()
    if guess > password:
        print("Your password is too high!")
        start()

start()
