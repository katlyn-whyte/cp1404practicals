from musician import Musician
from guitar import Guitar


class Band:
    def __init__(self, name=""):
        super().__init__(name)
        self.name = name
        self.members = []

    def __repr__(self):
        return str(vars(self))

    def __str__(self):
        super().__str__(Musician, Guitar)
        return f"{self.name}"

    def add(self, member):
        return self.members.append(member)
