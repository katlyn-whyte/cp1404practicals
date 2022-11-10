from prac_07.guitar import Guitar

CURRENT_YEAR = 2022


def main():
    in_file = open("guitars.csv", "a")
    guitars = []
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, ${guitar.cost}")

    in_file.close()
