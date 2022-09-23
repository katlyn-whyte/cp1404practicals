LENGTH = 4


def main():
    password = input("enter a password: ")


while len(password) != LENGTH:
    if len(password) >= LENGTH:
        print('*' * len(password))
    else:
        print("invalid password")
    password = input("enter a password: ")

main()
