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