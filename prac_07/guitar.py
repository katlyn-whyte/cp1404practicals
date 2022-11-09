CURRENT_YEAR = 2022


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost:.2f}"

    # def get_age(self):
    #     age = CURRENT_YEAR - self.year
    #     return f"in {CURRENT_YEAR} the {self.name} is {age} years old"

    def __lt__(self, other, CURRENT_YEAR):
        return self.year <= CURRENT_YEAR
