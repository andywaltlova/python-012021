from faker import Faker


class Balik:
    def get_info(self):
        print(f"Příjemce balíku: {self.name}")
        print(f"Balík doručte na adresu: {self.address}")

    def __init__(self, name, address):
        self.name = name
        self.address = address


g = Faker("cs_CZ")
balik = Balik(g.name(), g.address())
balik.get_info()

g = Faker(["cs_CZ", "sk_SK"])
for i in range(5):
    print(f"Name: {g.name()}, Address: {g.address()}")
    print()
