user = {
    "first_name": "Jio",
    "age": 30,
    "birthday": "January 11 1994",
    "dogs": ["Chewy", "Choco"],
}
message = "This persons name is {} and his pets' names are {} and {}"
updatedUser = "This persons name changed to {}"


if user["first_name"] == "Jio" and "Choco" and "Chewy" in user["dogs"]:
    print(message.format(user["first_name"], user["dogs"][0], user["dogs"][1]))
elif user["first_name"] == "Carlo":
    print(updatedUser.format(user["first_name"]))
else:
    print("This user doesn't exist")

newDogs = ["Kratos", "Mimir", "Tyr"]

user["dogs"].insert(1, "Bambam")
user["dogs"].append("Atreus")
user["dogs"].extend(newDogs)
user["dogs"].remove("Bambam")
del user["dogs"][4]

print(user["dogs"])
