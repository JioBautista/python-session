user = "Carlo"
age = 30
birthday = "January 11 1994"
text = "This user's name is {} and the person's age is {}"

if user == "Jio" and age == 30:
    print(text.format(user,age))
elif user != "Jio":
    print("Not the current user")
else:
    print("error")

list1 = [1,2,3]
list2 = [1,2,3]

user1 = 10
user2 = 10
if user1 is user2:
    print("user1 and user2 are the same")



if list1 is list2:
    print("list1 and list2 are the same object.")
else:
    print("Error")