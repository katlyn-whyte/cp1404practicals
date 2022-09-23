"""
CP1404/CP5632 - Practical
Temperature conversions
"""


# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit : "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(calculate_fahrenheit)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(calculate_celsius)
        else:
            print("invalid option")
        print(MENU)
        choice = input(">>>").upper()


def calculate_fahrenheit(fahrenheit):
    fahrenheit_to_celsius = 5 / 9 * (fahrenheit - 32)
    return fahrenheit_to_celsius


def calculate_celsius(celsius):
    celsius_to_fahrenheit = celsius * 9.0 / 5 + 32
    return celsius_to_fahrenheit


main()


# def main():
#     celsius = float(input("Celsius: "))
#     fahrenheit = float(input("Fahrenheit: "))
#
#
# def calculate_fahrenheit(fahrenheit):
#     fahrenheit_to_celsius = 5 / 9 * (fahrenheit - 32)
#     return fahrenheit_to_celsius
#
#
# def calculate_celsius(celsius):
#     celsius_to_fahrenheit = celsius * 9.0 / 5 + 32
#     return celsius_to_fahrenheit
#
#
# main()
