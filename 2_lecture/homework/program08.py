def valid_telephone_number(number:str):
    number = number.replace(' ', '')
    if len(number) not in [9, 13]:
        return False
    if len(number) == 13 and number[:4] != '+420':
        return False

    str_number = number.rstrip('+')
    if not str_number.isdigit():
        return False
    return True

def count_price_of_message(msg):
    return 3 * (len(msg) // 180 + 1)


tel_cislo = input('Zadej telefonni cislo: ')
if valid_telephone_number(tel_cislo):
    zprava = input('Zadej zpravu: ')
    print(f"Vysledna cena sms: {count_price_of_message(zprava)} Kč.")
else:
    print('Telefoni cislo ma spatny format.')