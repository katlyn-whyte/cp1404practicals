from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print(add_guitar, "added.")

    if guitars:
        guitars.sort()
        print("These are my guitars")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars, go buy one")


main()
