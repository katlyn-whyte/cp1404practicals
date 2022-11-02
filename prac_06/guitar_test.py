from prac_06.guitar import Guitar
CURRENT_YEAR = 2022


def run_tests():
    name = "Gibson L-5 class."
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2003, 1436.8)

    print(f"{guitar.name} get_age() - expected{95}. got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - expected{5}. got {guitar.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - expected {True}. got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - expected {False}. got {guitar.is_vintage()}")


if __name__ =='__main__':
    run_tests()