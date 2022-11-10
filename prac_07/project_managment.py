from prac_07.project import Project

MENU_STRING = "(L)oad projects\n(S)ave project\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new peojects\n(U)pdate projects\n(Q)uit"


def main():
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_project()
        elif choice == "S":
            print("S")
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            print("filter")
        elif choice == "A":
            print("add")
        elif choice == "U":
            print("update")
        else:
            print("Invalid menu choice")
            print(MENU_STRING)
        choice = input(">>> ").upper


def load_project():
    in_file = open("projects.txt", "r")
    projects = []
    for line in in_file:
        line = line.strip()
        parts = line.split(',')
        projects.append(parts)
        for project in projects:
            print(f"{project[0]}, {project[2]}, {project[3]}, {project[4]}")
        return projects

    # def save_project():


def display_project(projects):
    for project in projects():
        if project.completion_percentage < 100:
            print(project)
            return project


def filter_project(projects):
    for project in projects:
        if project.filter() < other.priority:
        print(project)
    #             def add_project():
    #                 def update_project():


main()
