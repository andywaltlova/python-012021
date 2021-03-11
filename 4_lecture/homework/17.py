class Polozka:
    def __init__(self, jmeno, zanr):
        self.jmeno = jmeno
        self.zanr = zanr

    def get_info(self):
        return f"Jmeno: {self.jmeno}\nZanr: {self.zanr}"


class Film(Polozka):
    def __init__(self, jmeno, zanr, delka):
        super().__init__(jmeno, zanr)
        self.delka = delka

    def get_info(self):
        delka_f = f"\nDelka: {self.delka}"
        return super().get_info() + delka_f

    def get_celkova_delka(self):
        return self.delka


class Serial(Polozka):
    def __init__(self, jmeno, zanr, pocet_epizod, delka_epizody):
        super().__init__(jmeno, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        delka_e = f"\nDelka epizody: {self.delka_epizody}"
        pocet_e = f"\nPocet epizod: {self.pocet_epizod}"
        return super().get_info() + delka_e + pocet_e

    def get_celkova_delka(self):
        return self.delka_epizody * self.pocet_epizod


class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.zhlednuto = []

    def zhledni_polozku(self, polozka):
        self.zhlednuto.append(polozka)

    def delka_sledovani(self):
        return sum([p.get_celkova_delka() for p in self.zhlednuto])


serial = Serial('Witcher', 'Fantasy', 8, 60)
film = Film('The Shawshank Redemption', 'Crime', 162)
uzivatel = Uzivatel('Andy')
uzivatel.zhledni_polozku(serial)
print(f'Po zhlednuti serialu: {uzivatel.delka_sledovani()} min.')
uzivatel.zhledni_polozku(film)
print(f'Po zhlednuti serialu i filmu: {uzivatel.delka_sledovani()} min.')
