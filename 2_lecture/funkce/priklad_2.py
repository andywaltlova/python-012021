"""Napiš funkci totalPrice, která vypočte cenu noci v hotelu. Funkce bude mít
dva parametry - persons (typ int) a breakfast (typ bool). Cena za noc za
osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou
cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3),
totalPrice(2, True). """


def total_price(persons, breakfast=False):
    price_per_person = 850
    if breakfast:
        price_per_person += 125
    return price_per_person * persons


print(total_price(3))
print(total_price(3, True))
