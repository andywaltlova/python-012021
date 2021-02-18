# Gustav je vášnivým čtenářem detektive z našeho nakladatelství a navíc si
# zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si
# eviduje - název knihy, počet stran a hodnocení od 0 do 10.
#
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

strany = 0
strany_hodnoceni_8 = 0
for book in books:
    if book['rating'] >= 8:
        strany_hodnoceni_8 += book['pages']
    strany += book['pages']

print('Celkem stran:', strany)
print('Stran s hodnocenim alespon 8:', strany_hodnoceni_8)
