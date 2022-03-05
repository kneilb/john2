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
name_list = ["Holly", "Andrew", "Michael", "Felix", "Archie", "Ellis", "Bella", "Charlie"]
name2 = random.choice(name_list)

# computer go
dice_list2 = dice_roll(times)
print()
print(f"{name2}'s roll.")
print(f"{dice_list2}")
total2 = sum(dice_list2)
print(f"{total2}")

winner()
