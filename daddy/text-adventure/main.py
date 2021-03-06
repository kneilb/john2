import copy

from typing import Optional

import items
import rooms

from player import Player
from rooms import Room



def get_command() -> str:
    print("What is your command?")
    return input("# ").lower()


def do_room(player: Player, room: Room) -> Optional[str]:
    room.intro()

    command = get_command()

    if player.command(command, room):
        return None

    new_room = room.command(command, player)

    if new_room:
        # print("I received room", new_room)
        pass
    else:
        print("I'm afraid that didn't seem to work!")

    print()  # put in a blank line so rooms are separated a bit.

    return new_room


def add_room(room: Room):
    locations[room.id()] = room


locations = {}


add_room(rooms.Cheese())
add_room(rooms.Haddock())
add_room(rooms.CrossRoads())
add_room(rooms.DeadEnd("north", "south"))
add_room(rooms.DeadEnd("south", "north"))
add_room(rooms.DeadEnd("east", "west"))
add_room(rooms.DeadEnd("west", "east"))
add_room(rooms.Win())
add_room(rooms.Death())

player = Player()
current_room = locations["cheese"]

while True:
    new_room = do_room(player, current_room)
    if new_room:
        current_room = locations[new_room]

# TODOs
# "user" commands" (including inventory) - needs to take room as a param (e.g. for drop)
# factor out moving out of rooms into Room (with a dict of directions -> room names)
# Make goat into its own class, probably a subclass of Object / Item or something similar?
# Add "look at" or "describe" commands, to get more detail about things
# Make items at a location part of Room
