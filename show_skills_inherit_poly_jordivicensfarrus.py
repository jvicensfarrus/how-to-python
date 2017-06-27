#Developed by Jordi Vicens Farrus

#In this exercices I want to show that I know how to use the inheritance and polymorphism.
class Product:
    def __init__(self, reference, name, price, description):
        self.reference = reference
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return """\
        REFERENCE\t{}
        NAME\t\t{}
        PRICE\t\t{}
        DESCRIPTION\t{}""".format(self.reference, self.name, self.price, self.description)

class Ornament(Product):
    pass

class Food(Product):
    producer = ""
    distributor = ""

    def __str__(self):
        return """\
        REFERENCE\t{}
        NAME\t\t{}
        PRICE\t\t{}
        DESCRIPTION\t{}
        PRODUCER\t{}
        DISTRIBUTOR\t{}""".format(self.reference, self.name, self.price, self.description, self.producer, self.distributor)

class Book(Product):
    number = ""
    author = ""

    def __str__(self):
        return """\
        REFERENCE\t{}
        NAME\t\t{}
        PRICE\t\t{}
        DESCRIPTION\t{}
        NUMBER\t\t{}
        AUTHOR\t\t{}""".format(self.reference, self.name, self.price, self.description, self.number, self.author)



orn = Ornament(2034, "Cup ornamented", 15, "Porcelain cup ornamented")

fo = Food(2035, "Oil bottle", 5, "250 ML")
fo.producer = "Spanish brand"
fo.distributor = "Distributions LTD"

bo = Book(2036, "Harry Potter", 9, "and the Chamber of Secrets")
bo.number = "0-123456-78-9"
bo.author = "J.K. Rowling"

products = [orn, fo]
products.append(bo)

for p in products:
    print(p)
#For show that I know how to use the data management
for p in products:
    if( isinstance(p, Ornament)):
        print(p.reference, p.name)
    elif( isinstance(p, Food)):
        print(p.reference, p.name, p.producer)
    elif( isinstance(p, Book)):
        print(p.reference, p.name, p.author)
