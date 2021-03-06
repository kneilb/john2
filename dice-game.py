import random
import time

# functions
def dice_roll(times):
    dice = []
    for a in range(times):
        dice.append(random.randint(1, 6))
    return dice

def winner():
    if total > total2:
        print(f"{name} wins!")
    else:
        print(f"{name2} wins!")

def roll_again(choices, list):
    print("rolling again...")
    time.sleep(random.randint(1, 3))
    for a in range (len(choices)):
        if choices[a] == "-":
            list[a] = random.randint(1, 6)

def computer_think1(fish): # roll everything
    option = ""
    for a in range(fish):
        option = option + "-"
    print(f"{name2} is thinking...")
    time.sleep(random.randint(7, 15))
    return option

def computer_think2(fish): # roll < 4
    option = ""
    for a in range(fish):
        if dice_list2[a] < 4:
            option = option + "-"
        else:
            option = option + "_"
    print(f"{name2} is thinking...")
    time.sleep(random.randint(7, 15))
    print(option)
    return option

# main
input("WELCOME TO THROW OFF!!! Press enter to continue!")
name = input("Enter your name: ")
times = input("Enter the amount of dice you shall use: ")
times = int(times)

print()
print("Waiting for a player...")
time.sleep(random.randint(1, 5))

dice_list = dice_roll(times)
print()
if name == "{;":
    opinion_film1 = input("Would you like to watch a film? ")
    if opinion_film1 == "yes" or "Yes" or "YES" or "fine" or "Fine" or "FINE":
        print(' {;"hi"    :) ')
        time.sleep(3)
        print(' {;      "time to get the goods":)')
        time.sleep(3)
        print('{;"got em"      :)')
        time.sleep(3)
        print('{;"arghhhh... HELP!!!"        =)')
        time.sleep(4)
        print('       "ha... thanks!"=)')
        time.sleep(3)

print(f"{name}'s roll.")
print(f"{dice_list}")
total = sum(dice_list)
print(f"{total}")

choice = input("Press _ to keep or - to throw again: ")
while len(choice) != times:
    print(f"You must enter {times} characters.")
    choice = input("Press _ to keep or - to throw again: ")
roll_again(choice, dice_list)
print(f"{dice_list}")
total = sum(dice_list)
print(f"{total}")

# computer code
name_list = ["Holly", "Andrew", "Michael", "Felix", "Archie", "Ellis", "Bella", "Charlie", "violet", "THRASHER123", "Best", "{;", "y0U n0oB"]
name2 = random.choice(name_list)

# computer go
time.sleep(4.444444444444444444444444444444444444444444444444444444444444444444444444444444444444)
dice_list2 = dice_roll(times)
print()
print(f"{name2}'s roll.")
print(f"{dice_list2}")
total2 = sum(dice_list2)
print(f"{total2}")
# future: decide on a strategy at random!
# which = ["computer_think1(times)", "computer_think2(times)"]
strategy = computer_think2(times)
roll_again(strategy, dice_list2)
print(f"{dice_list2}")

winner()
