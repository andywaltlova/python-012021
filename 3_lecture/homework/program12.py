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

    def get_info(self):
        return f"SPZ: {self.spz}\nTYP: {self.typ}"


peugeot = Auto('4A2 3020', 'Peugot 403 Cabrio', 47534)
skoda = Auto('1P3 4747', 'Skoda Octavia', 41253)

chce_pujcit = input("Jake auto chces pujcit? ")
if chce_pujcit == 'Škoda':
    print(skoda.get_info())
    skoda.pujc_auto()
elif chce_pujcit == "Peugeot":
    print(peugeot.get_info())
    peugeot.pujc_auto()
else:
    print(f'Auto ({chce_pujcit}) neni k dispozici.')
