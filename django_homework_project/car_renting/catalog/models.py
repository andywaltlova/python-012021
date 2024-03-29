from django.db import models
from django.utils import timezone


class Car(models.Model):
    license_plate = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    mileage = models.IntegerField()
    last_tech_inspection = models.DateTimeField()

    def __str__(self):
        return f'{self.license_plate} ({self.car_type})'

    @property
    def days_from_last_tech_inspection(self):
        now = timezone.now()  # Quite tricky to find
        result = now - self.last_tech_inspection
        return result.days


class Customer(models.Model):
    PROGRAMS = (
        ('R', 'Regular'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    driver_license_number = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    program = models.CharField(max_length=20, choices=PROGRAMS, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LoanRecord(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField()
    is_approved = models.BooleanField(default=False)

    # Foregin keys are here, because both relation are 1:N
    # (record refers to one car, but car can have multiple associated records)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)

    @property
    def state(self):
        now = timezone.now()  # Quite tricky to find

        if now > self.end:
            return 'PAST'
        elif now < self.start:
            return 'FUTURE'
        return 'CURRENT'
