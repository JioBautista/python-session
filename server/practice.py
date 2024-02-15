data = []


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class videoGameConsole(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand


class Games(Product):
    def __init__(self, name, price, year):
        super().__init__(name, price)
        self.year = year


def addProducts(name, price, brand):
    console = videoGameConsole(name, price, brand)
    data.append(
        {"Product name": console.name, "Price": console.price, "Brand": console.brand}
    )


def addGames(name, price, brand):
    games = Games(name, price, brand)
    data.append({"Game name": games.name, "Price": games.price, "Year": games.year})


addProducts("Playstation 4", 299.99, "Sony")
addProducts("Nintendo Switch", 499.99, "Nintendo")
addGames("God of War Ragnarok", 79.99, "2023")

for x in data:
    print(x)
