class Auto:
    def __init__(self, spz, typ, km):
        self.spz = spz
        self.typ = typ
        self.km = km
        self.je_volne = True

    def pujc_auto(self):
        if self.je_volne:
            self.je_volne = False
            return "Potvrzuji zapůjčení vozidla"
        return "Vozidlo není k dispozici"

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        if pocet_dni < 7:
            cena = 400 * pocet_dni
        else:
            cena = 300 * pocet_dni
        self.je_volne = True
        return f"Cena za vypujceni je {cena} Kč."

    def get_info(self):
        return f"SPZ: {self.spz}\nTYP: {self.typ}"

peugeot = Auto('4A2 3020', 'Peugot 403 Cabrio', 47534)
skoda = Auto('1P3 4747', 'Skoda Octavia', 41253)

chce_pujcit = input("Jake auto chces pujcit? ")
if chce_pujcit == 'Škoda':
    print(skoda.get_info())
    skoda.pujc_auto()
    pujcene_auto = skoda
elif chce_pujcit == "Peugeot":
    print(peugeot.get_info())
    peugeot.pujc_auto()
    pujcene_auto = peugeot
else:
    print(f'Auto ({chce_pujcit}) neni k dispozici.')
    exit()

print("BrmBrm...")

tachometr = int(input("Kolik kilometru si najel? "))
pocet_dni = int(input("Jak dlouho jsi mel auto pujcene? "))
print(pujcene_auto.vrat_auto(tachometr, pocet_dni))


