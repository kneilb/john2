import random
import time

# function
def dice_roll(times):
    dice = []
    for a in range(times):
        dice.append(random.randint(1, 6))
    return dice

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

# computer code
name_list = ["Holly", "Andrew", "Michael", "Felix", "Raphiel", "Ellis", "Bella", "Charlie"]
name2 = random.choice(name_list)

# computer go
dice_list2 = dice_roll(times)
print()
print(f"{name2}'s roll.")
print(f"{dice_list2}")
total2 = sum(dice_list2)
print(f"{total2}")
