import time
# Chatty chat bot
print("I am a reallyyyyyyyyyyy chatty chat bot!")
print("I love to talk!!!")
name = input("What is your name?")
job = input(f"Okay {name} what is your job???")
print(f"WOW!!! I wish I did {job}!")
print("Being a robot is tiring...")
print("Night!")
input("Are you gone yet?")
print("GO AWAY I AM SLEEPING")
input("Finally... I hate talking to humans... SNORE SNORE SNORE")

# Evil chatbot
print("Hi I am INTELLIGENT AND EVIL CHATBOT")
digit = input("Give me a number...")
digit2 = input(f"Give me another number {name}...")
sum = int(digit) + int(digit2)
print(f"Your numbers together are {sum}")
year = input("What year is it?")

my_birth_year = int(year) - 284
print(f"oh yeh, I forgot, sorry.So if it is {year} and I am 284 I was born in {my_birth_year}!")
age = input(f"How old are you?")
your_birth_year = int(year) - int(age)
print(f"WOH!!! You were born in {your_birth_year}! Thats like, nothing in robot!!!")
print(f"Anyway you held me up for 99999999999999999 robot years so go away...")
input("I SAID GO AWAY")
input("Well, if you are going to stay then byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
print("*Vanishes*")
time.sleep(20)

# Mathy chatbot
print("Hi... my name is mathy chatbot!")
print()
print("I like doing maths!")
choice1 = input("Would you like to do a quiz?")
if choice1 == "yes":
    quiz1 = input("Is the Mariana trench the deepest area of sea on earth?")
    if quiz1 == "yes":
        print(f"WOW!!! I only knew that when I was 638! You are only {age}! {name}, you're a genius!")
    else:
        print(f"Well, now you know {name}.")
else:
    print(f"Oh, Goodbye then {name}.")




