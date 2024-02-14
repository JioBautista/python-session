# DATA variable

data = [
    {"user": "Jbautista", "age": 30},
    {"user": "Chewy", "age": 4},
    {"user": "Choco", "age": 3},
]


class NewUsers:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def createNewUser(username, password):
    newUser = NewUsers(username, password)
    data.append({"user": newUser.username, "password": newUser.password})


createNewUser("ChewyHumper", 1234)
createNewUser("ChocoChomper", 1234)
createNewUser("JBautista", 1234)

for x in data:
    print(x)
