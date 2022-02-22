import random
import time

input("WELCOME TO THROW OFF!!! Press enter to continue!")
name = input("Enter your name:")
times = input("Enter the amount of dice you shall use:")
print()
print("Waiting for a player...")
time.sleep(6)
times = int(times)

def dice_roll(times):
    dice = []
    for a in range(times):
        dice.append(random.randint(1, 6))
    return dice


dice_list = dice_roll(times)
print()
print(f"{name}'s roll.")
print(f"{dice_list}")
total = sum(dice_list)
print(f"{total}")

# computer code
name2 = ["Holly", "Andrew", "Michael", "Felix", "Raphiel", "Ellis", "Bella", "Charlie"]

# computer go
dice_list2 = dice_roll(times)
print()
print(f"{name2}'s roll.")
print(f"{dice_list2}")
total2 = sum(dice_list2)
print(f"{total2}")
