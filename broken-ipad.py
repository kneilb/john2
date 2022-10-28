import random
import time
password = random.randint(1, 100) #100

# google #
def gogle():
    print()
    gogle_search = input("What shall you search? ")
    print(f"Sorry, {gogle_search} is not valid.")
    exit_gogle = input("would you like to exit gogle? y for yes and n for no: ")
    if exit_gogle == "n":
        gogle()
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

def fish_catcher():
    fish_caught = ("You caught a fish!", "You caught a fish!", "You waited, but no fish came.")
    one = random.choice(fish_caught)
    two = random.choice(fish_caught)
    three = random.choice(fish_caught)
    time.sleep(3)
    print("where would you like to fish?")
    fishing_spot = input("1, 2 or 3? ")
    if fishing_spot == "1":
        print(one)
    elif fishing_spot == "2":
        print(two)
    elif fishing_spot == "3":
        print(three)
    else:
        print("what you SAY!??!")

##################
# COMPUTER IS ON #
##################
def computer_is_on():
    time.sleep(2.5)
    print()
    app_chosen = input("Would you like to use: gogle, gmail, fish catcher, cheese monkey simulator or the app store? ")
    if app_chosen == "gogle":
        gogle()
    elif app_chosen == "gmail":
        gmail()
    elif app_chosen == "fish catcher":
        fish_catcher()

# start #
def start():
    guess = input("Enter what you think is the password that is from 0 to 100: ")
    guess = int(guess)
    if guess == password:
        print("System online")
        time.sleep(1)
        computer_is_on()
    if guess < password:
        print("Your password is too low!")
        start()
    if guess > password:
        print("Your password is too high!")
        start()

fish_catcher()
# start()
