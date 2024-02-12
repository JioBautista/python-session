# THIS IS A LIST
dogs = ["Chewy", "Choco"]
dogs.insert(1, "Bambam")

# THIS IS A TUPLE
name = ("Jio", "Carlo")

# THIS IS A SET

age = {28, 29, 30}

# THIS IS A DICTIONARY
user = {
    "first": "Jio",
    "last": "Pacho",
    "age": 30,
    "birthdate": "January 11, 1994",
    "dogs": ["Chewy", "Choco"],
}

user.update({"dogs": ["Chewy", "Choco", "Bambam"]})

# STRING FORMATTING
message = "This persons name is {}"

# IF STATEMENT
if "Jio" in name:
    print(message.format(name[0]))
if "dogs" in user:
    print("Key exists")

# FOR LOOPS
for keys in user.keys():
    print(keys)
for values in user.values():
    print(values)
for items in user.items():
    print(items)
