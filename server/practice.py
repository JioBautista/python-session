data = []


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


def createUser(username, password, email):
    user = User(username, password, email)
    data.append(
        {"username": user.username, "password": user.password, "email": user.email}
    )


def changePassword(user, newPass):
    for x in data:
        if user == x["username"]:
            x["password"] = newPass


createUser("Jbautista", 1234, "pachojio@gmail.com")
createUser("Chewy", 1234, "Chewy@gmail.com")
createUser("Choco", 1234, "Choco@gmail.com")
changePassword("Jbautista", 325002350)

for x in data:
    print(x)
