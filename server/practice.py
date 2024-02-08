import sys

data = [11, "Jio", 30]

users = {
    "firstName" : "Carlo",
    "birthday": "January 11 1994",
    "age": 21
}

if users["firstName"] == "Jio" or users["age"] == 30:
    print("Correct information")
else:
    print("Incorrect information")


print( 29 in data )