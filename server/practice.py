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

age = 30
name = "Jio"
country = "Philippines"
txt = "Hello my name is {} and I am {} years old. I was born in {}"

print(txt.format(name, age, country))