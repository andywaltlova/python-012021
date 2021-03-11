class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered} '


class Driver:
    def __init__(self, name):
        self.name = name
        self.package_list = []

    def assign_package(self, package):
        if package.delivered:
            print('Balik nelze priradit, uz byl dorucen.')
        else:
            self.package_list.append(package)

    def remaining_packages(self):
        return len(self.package_list)


balik = Package('Brno', 200)
balik2 = Package('Praha', 200)

ridic = Driver('Martin')
print(ridic.remaining_packages())
ridic.assign_package(balik)
print(ridic.remaining_packages())
ridic.assign_package(balik2)
print(ridic.remaining_packages())
