from datetime import datetime


class Kontakt:
    def __init__(self, jmeno, email):
        self.jmeno = jmeno
        self.email = email


class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = ""

    def uloz_zapis(self, zapis):
        if datetime.now() > self.datum_pohovoru:
            self.zapis_z_pohovoru = zapis
            print('Zapis ulozen.')
        else:
            print('[ERROR] Pohovor jeste neprobehl.')


datum_pohovoru_OK = datetime(2020, 10, 25)
datum_pohovoru_NOK = datetime(2022, 10, 25)

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru_OK)
uchazec.uloz_zapis("Prijat")

uchazec = Uchazec('Andy', 'example@email.com', datum_pohovoru_NOK)
uchazec.uloz_zapis("Prijat")
