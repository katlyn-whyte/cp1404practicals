# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")


def main():
    score = float(input("enter your score: "))



def score_results(score):
    if score > 100:
        print("invalid score")
    elif score >= 90:
        print("excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")

