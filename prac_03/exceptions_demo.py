"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?:
value error will occur if a number is not entered into either the numerator or the denominator,
or a word value is entered instead of a number.

2. When will a ZeroDivisionError occur?:
zero division will occur when any number is entered into the numerator and zero
is entered as the denominator as no number is divisible by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?:

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
