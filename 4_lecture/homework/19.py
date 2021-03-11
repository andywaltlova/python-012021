from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = 10
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

mena = input('Zadej menu, kterou chces prevest na bitcoiny: ')
pocet = int(input('Zadej pozadovany pocet bitcoinu: '))

b = BtcConverter()
b_kurz = b.get_latest_price(mena)

print(f"K ziskani {pocet} B je potreba {pocet * b_kurz} {mena}")
