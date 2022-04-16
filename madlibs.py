import random
verbs = ["jumped", "teleported", "ran", "dropped", "fell", "flew", "used majicyness to appear"]
input("WELCOME TO MAD LIBS press enter to play!")
animal = input("Give me the name of an animal... ")
colour = input("Give me a colour... ")
description = input("Give me an adjective for an object... ")
verb = random.choice(verbs)
print()
sentence = [
    f"The {colour} {animal} {verb} into the {description} hedge!",
    f"The {description} {animal} exploded and {verb} onto the {colour} rock!",
    f"The {animal} fell into the {colour}, {description} bush!",
    f"The {colour} dumper truck was attacked by the {description} {animal}!",
    f"The giant, {description} {animal} attacked the {colour} house!",
    f"The dog and the {animal} went into the {description}, {colour} castle!",
    f"The {description} {animal} was shot by a man wearing a {colour} coat!",
    f"The strange {animal} flew into the {colour} sky as a {description} rock {verb} on its head and killed it!",
    f"The {colour} {animal} {verb} onto the {description} tree!",
    f"The man threw a {animal} onto a {description} ledge above a pit of {colour} deer!",
    f"The {colour} man threw the {description} rock at the {animal}!",
    f"The {description} boulder crushed the {animal} who {verb} on a {colour} tree!"
]
print(random.choice(sentence))
