class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def get_net_salary(self):
        return self.salary - self.get_tax()

    def get_tax(self):
        return self.salary * 0.15 - self.children * 1500

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children
