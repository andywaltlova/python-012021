class Employee:
    def __init__(self, name, position, probation):
        self.name = name
        self.position = position
        self.remaining_days = 25
        self.probation = probation

    def take_holiday(self, days):
        if self.remaining_days >= days:
            self.remaining_days -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remaining_days} dní."

    def get_info(self):
        msg = f"{self.name} pracuje na pozici {self.position}."
        if self.probation:
            return msg + ' Je ve zkusebni dobe.'
        return msg