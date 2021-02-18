sklad = {
    "1N4148": 250,
    "BAV21": 54,
    "KC147": 147,
    "2N7002": 97,
    "BC547C": 10
}

kod = input('Zadej kod: ')
mnozstvi = int(input('Zadej mnozstvi: '))

if kod in sklad:
    na_sklade = sklad[kod]

    if mnozstvi > na_sklade:
        print('Na sklade neni dostatek kusu, proto muzeme prodat maximalne:',
              sklad[kod])
        sklad[kod] = 0
    else:
        print('Poptavku je mozne uspokojit v plne vysi')
        sklad[kod] -= mnozstvi
else:
    print('Soucastka neni skladem.')
