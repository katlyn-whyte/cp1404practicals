for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# B
for i in range(21, 0, -1):
    print(i, end=' ')
print()

# C
number_of_stars = int(input("number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# D
number_of_stars = int(input("number of stars: "))
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
