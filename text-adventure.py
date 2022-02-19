
print("You are in a room full of cheese.")

while True:
    print("What is your command?")
    command = input("# ")

    if "cheese" in command and "eat" in command:
        print("You eat the cheese, and fall down a massive hole to the next room")
        break

    print("Sorry, I didn't understand!")

print("You are in a room full of haddock.")

while True:
    print("What is your command?")
    command = input("# ")

    if ("fish" in command or "catch" in command) and "haddock" in command:
        print("You catch the haddock. It eats you all up!")
        print("You win!")
        exit(1)

    print("Sorry, I didn't understand!")
