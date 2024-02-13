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

# STRING FORMATTING
message = "This persons name is {}, his age is {}, his birthday is {} and his pets names are {}"


#  FUNCTIONS
def keyNames(fName, lName):
    print("This persons first name is " + fName + " and last name is " + lName)


keyNames(fName="Jio", lName="Pacho")
