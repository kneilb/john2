import copy

from typing import Optional

from items import Item, Lantern
from player import Player

class Room(object):
    def __init__(self, id="default", intro="default room!", exits={}, items={}):
        self._id = id
        self._intro = intro
        self._exits = exits
        self._items = copy.deepcopy(items)

    def id(self):
        return self._id

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

            return self._id

        return None

    def add_item(self, item):
        self._items[item.id] = item

    def remove_item(self, item_name: str) -> Optional[Item]:
        return self._items.pop(item_name, None)


class Cheese(Room):
    def __init__(self):
        lantern = Lantern()
        super().__init__(
            "cheese",
            "You are in a room full of cheese.",
            {},
            {
                lantern.id: lantern
            }
        )

    def command(self, command: str, player: Player) -> Optional[str]:
        if "cheese" in command and "eat" in command:
            print("You eat the cheese, and fall down a massive hole to the next room")
            return "haddock"

        return super().command(command, player)


class Haddock(Room):
    def __init__(self):
        super().__init__("haddock", "You are in a room, featuring a pool containing a huge haddock.")

    def command(self, command: str, player: Player) -> Optional[str]:
        if ("fish" in command or "catch" in command) and "haddock" in command:
            print("You attempt to catch the haddock. It eats you all up!")
            print("Then it sneezes, and you are thrown into the air!")
            print("After a long flight, you find yourself landing at a new location.")
            return "crossroads"

        return super().command(command, player)


class CrossRoads(Room):
    def __init__(self):
        self.has_goat = True
        self.goat_alive = True
        self.goat_fed = False

        super().__init__(
            "crossroads",
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
                if self.goat_fed:
                    print("It is looking quite chubby.")
            else:
                print("There is an ex-goat here. It is not looking very well, and it smells a bit.")
    
    def command(self, command: str, player: Player):
        if self.has_goat and self.goat_alive and "goat" in command:
            if "speak" in command or "talk" in command:
                print("The goat seems interested, but struggles to communicate.")
                if self.goat_fed:
                    print("It makes some happy bleating noises.")
                return "crossroads"

            if ("feed" in command or "give" in command) and ("cheese" in command or "haddock" in command):
                print("The goat happily munches up the food you offer it.")
                self.goat_fed = True
                return "crossroads"

            if "shoot" in command:
                print("You shoot at the goat, but miss and hit yourself in the knee.")
                return "die"

            if "kill" in command:
                print("You manage to kill the goat with your bear hands (sic).")
                self.goat_alive = False
                return "crossroads"

        return super().command(command, player)


class DeadEnd(Room):
    def __init__(self, id, exit_dir):
        super().__init__(
            id,
            "You find yourself at a dead end.",
            {
                exit_dir: "crossroads"
            }
        )


class Death(Room):
    def __init__(self):
        super().__init__("death")

    def intro(self):
        print("You die! Please leave immediately.")
        exit(0)


class Win(Room):
    def __init__(self):
        super().__init__("win")

    def intro(self):
        print("You win! Did you cheat?!")
        exit(0)
