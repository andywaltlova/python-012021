prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

nazev_knihy = input('Zadej nazev knihy: ')
prodej = 0
if nazev_knihy in prodeje2019:
    prodej += prodeje2019[nazev_knihy]
if nazev_knihy in prodeje2020:
    prodej += prodeje2020[nazev_knihy]
print('Prodano kusu:', prodej)


# 2. varianta
prodej = prodeje2020.get(nazev_knihy, 0) + prodeje2019.get(nazev_knihy, 0)
print('Prodano kusu:', prodej)
