import random

NUMBERS_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many picks: "))
    while number_of_quick_picks < 0:
        print("invalid pick")
        number_of_quick_picks = int(input("How many picks: "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_IN_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print("".join(f"{number:4}" for number in quick_pick))


main()
