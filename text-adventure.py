def get_command():
    print("What is your command?")
    return input("# ")


def do_room(player, room):
    room.intro()

    command = get_command()

    if player.command(command):
        return

    new_room = room.command(command)

    if new_room:
        # print("I received room", new_room)
        pass
    else:
        print("I'm afraid that didn't seem to work!")

    print()  # put in a blank line so rooms are separated a bit.

    return new_room


class Player(object):
    def __init__(self):
        self._items = {}

    def command(self, command):
        if command in ["i", "inv", "inventory"]:
            if self._items:
                print("You are carrying:")
                for k, v in self._items:
                    print(f"{k} {v}")
            else:
                print("Your pockets are empty!")
            print()

            return True

        if "drop" in command:
            item = command.split(" ")[-1]
            if item not in self._items:
                print("Sorry, you don't seem to be carrying one of those!")
                return True

        return False


class Item(object):
    pass


class Goat(Item):
    pass


class Room(object):
    def __init__(self, intro="default room!", exits={}):
        self._intro = intro
        self._exits = exits

    def intro(self):
        print(self._intro)

        if self._exits:
            if len(self._exits) == 1:
                start = "is an exit"
            else:
                start = "are exits"
            exits = ", ".join(list(self._exits.keys()))
            print(f"There {start} to the {exits}.")
        else:
            print("There are no obvious exits.")

    def command(self, command):
        if command in self._exits:
            return self._exits[command]

        return None


class CheeseRoom(Room):
    def __init__(self):
        super().__init__("You are in a room full of cheese.")

    def command(self, command):
        if "cheese" in command and "eat" in command:
            print("You eat the cheese, and fall down a massive hole to the next room")
            return "haddock"

        return super().command(command)


class HaddockRoom(Room):
    def __init__(self):
        super().__init__("You are in a room, featuring a pool containing a huge haddock.")

    def command(self, command):
        if ("fish" in command or "catch" in command) and "haddock" in command:
            print("You attempt to catch the haddock. It eats you all up!")
            print("Then it sneezes, and you are thrown into the air!")
            print("After a long flight, you find yourself landing at a new location.")
            return "crossroads"

        return super().command(command)


class CrossRoadsRoom(Room):
    def __init__(self):
        self.has_goat = True
        self.goat_alive = True

        super().__init__(
            "You are at a crossroads.",
            {
                "north": "north",
                "south": "south",
                "east": "east",
                "west": "west"
            }
        )

    def intro(self):
        super().intro()

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

            if "take" in command or "carry" in command or "pick up" in command:
                print("You pick up the goat")
                self.has_goat = False
                return "crossroads"

        return super().command(command)


class DeadEndRoom(Room):
    def __init__(self, exit_dir):
        super().__init__(
            "You find yourself at a dead end.",
            {
                exit_dir: "crossroads"
            }
        )


class DeathRoom(Room):
    def intro(self):
        print("You die! Please leave immediately.")
        exit(0)


class WinRoom(Room):
    def intro(self):
        print("You win! Did you cheat?!")
        exit(0)


rooms = {
    "cheese": CheeseRoom(),
    "haddock": HaddockRoom(),
    "crossroads": CrossRoadsRoom(),
    "north": DeadEndRoom("south"),
    "south": DeadEndRoom("north"),
    "east": DeadEndRoom("west"),
    "west": DeadEndRoom("east"),
    "win": WinRoom(),
    "death": DeathRoom()
}

player = Player()
current_room = rooms["cheese"]

while True:
    new_room = do_room(player, current_room)
    if new_room:
        current_room = rooms[new_room]

# TODOs
# "user" commands" (including inventory) - needs to take room as a param (e.g. for drop)
# factor out moving out of rooms into Room (with a dict of directions -> room names)
# Make goat into its own class, probably a subclass of Object / Item or something similar?
# Add "look at" or "describe" commands, to get more detail about things
# Make items at a location part of Room
