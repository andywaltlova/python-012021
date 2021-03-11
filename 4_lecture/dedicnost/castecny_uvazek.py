class Employee:
    def take_holiday(self, days):
        if self.remainingHolidayDays >= days:
            self.remainingHolidayDays -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."

    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.remainingHolidayDays = 25


class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload

    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}. Uvazek: {self.workload}"


brigadnik = PartTimeEmployee('Karel', 'Udrzbar', 0.5)
print(brigadnik.get_info())
