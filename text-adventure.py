def get_command():
    print("What is your command?")
    return input("# ")


def do_room(room):
    room.intro()

    command = get_command()

    new_room = room.command(command)

    if new_room:
        # print("I received room", new_room)
        pass
    else:
        print("I'm afraid that didn't seem to work!")

    print()  # put in a blank line so rooms are separated a bit.

    return new_room


class Room(object):
    def __init__(self, intro="default room!"):
        self._intro = intro

    def intro(self):
        print(self._intro)

    def command(self, command):
        return None


class CheeseRoom(Room):
    def __init__(self):
        super().__init__("You are in a room full of cheese.")

    def command(self, command):
        if "cheese" in command and "eat" in command:
            print("You eat the cheese, and fall down a massive hole to the next room")
            return "haddock"

        return None


class HaddockRoom(Room):
    def __init__(self):
        super().__init__("You are in a room full of haddock.")

    def command(self, command):
        if ("fish" in command or "catch" in command) and "haddock" in command:
            print("You catch the haddock. It eats you all up!")
            return "win"

        return None

class WinRoom(Room):
    def intro(self):
        print("You win! Please leave immediately.")
        exit(0)

rooms = {
    "cheese": CheeseRoom(),
    "haddock": HaddockRoom(),
    "win": WinRoom()
}

current_room = rooms["cheese"]

while True:
    new_room = do_room(current_room)
    if new_room:
        current_room = rooms[new_room]
