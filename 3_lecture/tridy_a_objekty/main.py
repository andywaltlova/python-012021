# 1
class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f'Kniha se jmenuje {self.title} a ma {self.pages} stranek a stoji {self.price} Kc.'

    def discount(self, amount):
        self.price -= self.price * (amount / 100)


# kniha = Book('Harry Potter', 350, 250)
# print(kniha.get_info())
# kniha.discount(50)
# print(kniha.get_info())


# 2
class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        # return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

        dorucenost = 'nebyl'
        if self.delivered:
            dorucenost = 'byl'
        return f'Balik na adresu {self.address} s vahou {self.weight} kg a {dorucenost} dorucen.'


# balik = Package('Brno 23',250)
# print(balik.get_info())
# balik.deliver()
# print(balik.get_info())


# 3
class Employee:
    def __init__(self, name, position, probation):
        self.name = name
        self.position = position
        self.remaining_days = 25
        self.probation = probation

    def take_holiday(self, days):
        if self.remaining_days >= days:
            self.remaining_days -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remaining_days} dní."

    def get_info(self):
        msg = f"{self.name} pracuje na pozici {self.position}."
        if self.probation:
            return msg + ' Je ve zkusebni dobe.'
        return msg
