baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input('Zadej kod baliku: ')

if kod_baliku in baliky:
    print('Balik byl predan kuryrovi')
else:
    print('Balik nebyl predan kuryrovi')
