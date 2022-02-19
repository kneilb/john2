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
            print("Then it sneezes, and you are thrown into the air!")
            print("After a long flight, you find yourself landing at a new location.")
            return "crossroads"

        return None


class CrossRoadsRoom(Room):
    def __init__(self):
        self.has_goat = True
        self.goat_alive = True

    def intro(self):
        print("You are at a crossroads.")
        print("There are exits to the north, south, east and west.")

        if self.has_goat:
            print()
            if self.goat_alive:
                print("There is a goat here.")
            else:
                print("There is an ex-goat here. It is not looking very well, and it smells a bit.")
    
    def command(self, command):
        if self.has_goat and self.goat_alive and "goat" in command:
            if "speak" in command or "talk" in command:
                print("The goat seems interested, but struggles to communicate.")
                print("It makes some happy bleating noises.")
                return "crossroads"

            if ("feed" in command or "give" in command) and ("cheese" in command or "haddock" in command):
                print("The goat happily munches up the food you offer it.")
                return "win"

            if "shoot" in command:
                print("You shoot at the goat, but miss and hit yourself in the knee.")
                return "die"

            if "kill" in command:
                print("You manage to kill the goat with your bear hands (sic).")
                self.goat_alive = False
                return "crossroads"

            if "take" in command or "carry" in command:
                print("You pick up the goat")
                self.has_goat = False
                return "crossroads"

        if "north" in command:
            return "death"
        
        if "south" in command:
            return "death"

        if "east" in command:
            return "death"

        if "west" in command:
            return "death"


class DeathRoom(Room):
    def intro(self):
        print("You die! Please leave immediately.")
        exit(0)


class WinRoom(Room):
    def intro(self):
        print("You win! Please leave immediately.")
        exit(0)


rooms = {
    "cheese": CheeseRoom(),
    "haddock": HaddockRoom(),
    "crossroads": CrossRoadsRoom(),
    "win": WinRoom(),
    "death": DeathRoom()
}

current_room = rooms["cheese"]

while True:
    new_room = do_room(current_room)
    if new_room:
        current_room = rooms[new_room]
