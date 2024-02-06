import sys

users = {
    "firstName" : "Carlo",
    "age": 21,
    "birthday": "January 11 1994"
}

if users["firstName"] == "Jio" or users["age"] == 30:
    print("Correct information")
else:
    print("Incorrect information")

playerchoice = input("""Enter...
     1 for Rock,
     2 for Paper,
     3 for Scissors: """)

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3.")