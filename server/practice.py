first_name = "Jio Carlo"
first_pet = "Chewy"
second_pet = "Choco"
birth_date = 1111994
first_pet_birth_date = str(4212019)
second_pet_birth_date = 7132020


isAdmin = True


# TERNARY OPERATOR
# print("Welcome Admin user: " +first_name) if isAdmin == True else print("Welcome User")

if isAdmin == True:
    print("Welcome Admin " +first_name.upper())
else:
    print("Unauthorized user")

print(first_name[0:3])

gpa = 4.3

print(round(gpa))

print(round(gpa, 1))