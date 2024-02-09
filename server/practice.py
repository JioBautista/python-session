user = {
    "first_name": "Jio",
    "age": 30,
    "birthday": "January 11 1994",
    "dogs": ["Chewy", "Choco"],
}
message = "This persons name is {} and his pets' names are {} and {}"

user["first_name"] = "Carlo"

if user["first_name"] == "Jio":
    print(message.format(user["first_name"], user["dogs"[0]]))
else:
    print("This person doesn't exist")
