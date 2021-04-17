from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    mileage = models.IntegerField()
    last_tech_inspection = models.DateTimeField()


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    driver_license_number = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class Borrowing(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField()
