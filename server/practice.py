from data import users
from data import products


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


class Shoes(Product):
    pass


def addProducts(name, price, brand):
    console = videoGameConsole(name, price, brand)
    products.append(
        {"Product name": console.name, "Price": console.price, "Brand": console.brand}
    )


def addGames(name, price, brand):
    global msg
    msg = "Hello World!"
    games = Games(name, price, brand)
    products.append({"Game name": games.name, "Price": games.price, "Year": games.year})


def addShoes(name, price):
    shoes = Shoes(name, price)
    products.append({"Shoe name": shoes.name, "Shoe Price": shoes.price})


addProducts("Playstation 4", 299.99, "Sony")
addProducts("Nintendo Switch", 499.99, "Nintendo")
addGames("God of War Ragnarok", 79.99, "2023")
addShoes("Converse Chuck Tailor", 99.99)


print(products)
