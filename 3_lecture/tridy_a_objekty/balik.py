class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        # return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

        dorucenost = 'nebyl'
        if self.delivered:
            dorucenost = 'byl'
        return f'Balik na adresu {self.address} s vahou {self.weight} kg a {dorucenost} dorucen.'


balik = Package('Brno 23',250)
print(balik.get_info())
balik.deliver()
print(balik.get_info())

