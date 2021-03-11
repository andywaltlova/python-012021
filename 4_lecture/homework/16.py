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


class Serial(Polozka):
    def __init__(self, jmeno, zanr, pocet_epizod, delka_epizody):
        super().__init__(jmeno, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_info(self):
        delka_e = f"\nDelka epizody: {self.delka_epizody}"
        pocet_e = f"\nPocet epizod: {self.pocet_epizod}"
        return super().get_info() + delka_e + pocet_e


serial = Serial('Witcher', 'Fantasy', 8, 60)
print(serial.get_info())
film = Film('The Shawshank Redemption', 'Crime', 162)
print(film.get_info())
