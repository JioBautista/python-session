user = {
    "first_name": "Jio",
    "age": 30,
    "birthday": "January 11 1994",
    "dogs": ["Chewy", "Choco"],
}
newUser = {
    ("Jio", "Pacho"): {"age": 30, "birthday": "January 11, 1994"},
    ("John", "Doe"): {"age": 30, "birthday": "December 11 1990"},
}
message = "This persons name is {} and his pets' names are {} and {}"
updatedUser = "This persons name changed to {}"


if user["first_name"] == "Jio" and "Choco" and "Chewy" in user["dogs"]:
    print(message.format(user["first_name"], user["dogs"][0], user["dogs"][1]))
elif user["first_name"] == "Carlo":
    print(updatedUser.format(user["first_name"]))
else:
    print("This user doesn't exist")

newDogs = ["Kratos", "Mimir", "Tyr", "BamBam"]

user["dogs"].extend(newDogs)
dogsCopy = user["dogs"].copy()
dogsCopy.append("Odin")

for x in newUser:
    if "Jio" in x:
        print("correct")
    elif "John" in x:
        print("Also correct")
    else:
        print("Don't exist")
