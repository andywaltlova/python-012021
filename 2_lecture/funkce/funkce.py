#1

def mult(a, b):
    return a * b

# 2

def total_price(persons, breakfast=False):
    cena = persons * 850
    if breakfast:
        cena += persons * 125
    return cena

#print(total_price(10, breakfast=True))


def mont_of_birth(n):
    # month = n[2:4]
    month = n[2] + n[3]
    month = int(month)
    if month > 50:
        month -= 50
    #month = month % 50
    return month

#print(mont_of_birth('9507125899'))

import random
def roulette(row, bet):
    n = random.randint(0, 36)
    print(f'Padlo cislo: {n}')

    if n == 0:
        return 0
    if n % 3 == 1 and row == 1:
        return bet * 2
    if n % 3 == 2 and row == 2:
        return bet * 2
    if n % 3 == 0 and row == 3:
        return bet * 2
    return 0


row = int(input('Zadej na jakou radu chces vsadit: '))
bet = int(input('Zadej kolik chces vsadit: '))

print(roulette(row, bet))
