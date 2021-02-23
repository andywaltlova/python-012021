"""
Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. 
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
"""


def month_of_birth(birth_number):
    month = birth_number[2] + birth_number[3]
    month = int(month)
    month = month % 50
    return month


print(month_of_birth("9555125899"))
