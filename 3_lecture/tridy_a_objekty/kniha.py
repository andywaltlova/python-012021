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


kniha = Book('Harry Potter', 350, 250)
print(kniha.get_info())
kniha.discount(50)
print(kniha.get_info())
