import random


def main():
    print("Hello, I am Daddy the chatbot!")
    print("I like cheese, ninjas, goats and pirates!!")
    print()
    print("I also enjoy talking about badgers.")
    print()

    name = do_intro()
    print()

    topics = [
        do_badgers,
        do_goats,
        do_ninjas,
        do_pet,
        do_pirates
    ]

    random.shuffle(topics)

    while topics:
        func = topics.pop()
        func()
        print()

    do_bedtime(name)


def do_intro():
    name = input("What is your name? ")
    print(f"Hello {name}, it's a pleasure to meet you!")

    return name


def pluralise(noun):
    if len(noun) >= 1 and noun[-1] != "s":
        if noun[-1] == "h":
            noun += "es"
        else:
            noun += "s"

    return noun


def do_pet():
    animal = input("What is your favourite animal?! ")

    plural_animal = pluralise(animal)

    if plural_animal in ["goats", "fishes", "badgers"]:
        capital_plural_animal = plural_animal.capitalize()
        print(f"What?! {capital_plural_animal} are my favourite too!")
    else:
        print(f"Hmm, I quite like {plural_animal} too, although I wouldn't want to keep one as a pet!")


def do_ninjas():
    print("Ninjas are pretty scary, aren't they?!")
    while True:
        ninjas_string = input("How many ninjas would it take to make you run away?! ")
        try:
            num_ninjas = int(ninjas_string)
            break
        except Exception:
            print("Are you sure that was a number??")

    if num_ninjas <= 1:
        print("You scare pretty easily!")
    elif num_ninjas > 100:
        print("You are insanely brave!")
    else:
        print("I'd like to think I'm as brave as you...")


def do_goats():
    print("I really like goats, but some people think they smell!")
    opinion = input("What do you think of them?! ")
    print(f"Oh, that's a shame. Why do you think {opinion} about them?!")


def do_badgers():
    print("Badgers are amazing at digging holes, and eating things they find in bins!")
    option = input("Would you rather fight 100 budgie sized badgers, or one badger sized budgie?!")
    print("Crikey, you're brave!")
    print(f"Although, on reflection I think I'd rather fight {option}, too!")


def do_pirates():
    print("I really like dressing up as a pirate and boarding people's ships!")
    hobby = input("What's you favourite hobby?! ")

    print(f"Wow. That sounds really cool. I really like the idea of {hobby}, but it sounds hard!!")


def do_bedtime(name):
    print("Right, it's time for me to go to bed!")
    print(f"It was great to chat to you {name}!")


if __name__ == "__main__":
    main()
