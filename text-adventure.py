import copy

from typing import Optional


def get_command() -> str:
    print("What is your command?")
    return input("# ").lower()


def do_room(player, room):
    room.intro()

    command = get_command()

    if player.command(command, room):
        return

    new_room = room.command(command, player)

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

    def remove_item(self, name):
        return self._items.pop(name, None)

    def add_item(self, item):
        self._items[item.id] = item

    def command(self, command: str, room) -> bool:
        if command in ["i", "inv", "inventory"]:
            if self._items:
                print("You are carrying:")
                for k, v in self._items.items():
                    print(f"{k} {v}")
            else:
                print("Your pockets are empty!")
            print()

            return True

        if "drop" in command:
            item_name = command.split(" ")[-1]

            item = self.remove_item(item_name)
            if not item:
                print("Sorry, you don't seem to be carrying one of those!")
                return True

            print(f"You drop your {item_name}")

            room.add_item(item)

        return False


class Item(object):
    def __init__(self, id, description):
        self.id = id
        self._description = description

    def description(self):
        return self._description


class Lantern(Item):
    def __init__(self):
        super().__init__("lantern", "A lantern.")


class Goat(Item):
    def __init__(self):
        super().__init__("goat", "A goat.")

        self._alive = True
        self._decomposition = 0

    def description(self):
        super().description()
        if self._alive:
            print("It seems to be breathing.")
        else:
            print("It appears to be somewhat dead.")


class Room(object):
    def __init__(self, intro="default room!", exits={}, items={}):
        self._intro = intro
        self._exits = exits
        self._items = copy.deepcopy(items)

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

        if self._items:
            items = ", ".join(list(self._items.keys()))
            print(f"There are some items here: {items}")

    def command(self, command: str, player: Player) -> Optional[str]:
        if command in self._exits:
            return self._exits[command]

        if "pick up" in command or "take" in command:
            item_name = command.split(" ")[-1]
            item = self.remove_item(item_name)
            if not item:
                print("Sorry, I can't find one of those to pick up!")
            else:
                print(f"You pick up the {item_name}.")

            player.add_item(item)
            # TODO: return non-none! (id of current room...)

        return None

    def add_item(self, item):
        self._items[item.id] = item

    def remove_item(self, item_name: str) -> Optional[Item]:
        return self._items.pop(item_name, None)


class CheeseRoom(Room):
    def __init__(self):
        lantern = Lantern()
        super().__init__(
            "You are in a room full of cheese.",
            {},
            {
                lantern.id: lantern
            }
        )

    def command(self, command: str, player: Player) -> str:
        if "cheese" in command and "eat" in command:
            print("You eat the cheese, and fall down a massive hole to the next room")
            return "haddock"

        return super().command(command, player)


class HaddockRoom(Room):
    def __init__(self):
        super().__init__("You are in a room, featuring a pool containing a huge haddock.")

    def command(self, command: str, player: Player) -> str:
        if ("fish" in command or "catch" in command) and "haddock" in command:
            print("You attempt to catch the haddock. It eats you all up!")
            print("Then it sneezes, and you are thrown into the air!")
            print("After a long flight, you find yourself landing at a new location.")
            return "crossroads"

        return super().command(command, player)


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
    
    def command(self, command: str, player: Player):
        if self.has_goat and self.goat_alive and "goat" in command:
            if "speak" in command or "talk" in command:
                print("The goat seems interested, but struggles to communicate.")
                print("It makes some happy bleating noises.")
                return "crossroads"

            if ("feed" in command or "give" in command) and ("cheese" in command or "haddock" in command):
                print("The goat happily munches up the food you offer it.")
                return "crossroads"

            if "shoot" in command:
                print("You shoot at the goat, but miss and hit yourself in the knee.")
                return "die"

            if "kill" in command:
                print("You manage to kill the goat with your bear hands (sic).")
                self.goat_alive = False
                return "crossroads"

        return super().command(command, player)


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
