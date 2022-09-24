LENGTH = 4


def main():
    password = input("enter your password: ")

    get_password(password)


def get_password(password):
    while len(password) != LENGTH:
        if len(password) >= LENGTH:
            asterisks_print(password)
        else:
            print("invalid password length")
        password = input("enter a password: ")


def asterisks_print(password):
    print('*' * len(password))


main()
