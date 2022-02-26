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
