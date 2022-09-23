MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("enter name: ")
print(MENU_STRING)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("incorrect choice")
    print(MENU_STRING)
    choice = input(">>> ").upper()
print("finished.")
