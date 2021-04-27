from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models


class IndexView(View):
    def get(self, request):
        return HttpResponse(
            """
    <head>
    <meta charset="UTF-8">
    <title>Czechitas</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <style>
        html {font-family: 'Roboto', sans-serif;}
        h1 {text-align: center;}
    </style>
    </head>
    <p style="text-align: center">
    <a href="http://127.0.0.1:8000/catalog/">Home</a> |
    <a href="http://127.0.0.1:8000/catalog/cars">Cars</a> |
    <a href="http://127.0.0.1:8000/catalog/loans">Loans</a> |
    <a href="http://127.0.0.1:8000/catalog/customers">Customers</a>
    </p>
    <h1 style='text-align:center'>Welcome to our car rental!</h1>
    <p style='text-align:center'>Our rental shop was established in 2011 and today offers approximately 30 cars.</p>
    """
        )


class CarsView(ListView):
    model = models.Car
    template_name = 'car_template.html'


class LoansView(ListView):
    model = models.LoanRecord
    template_name = 'loan_template.html'


class CustomerView(ListView):
    model = models.Customer
    template_name = 'customer_template.html'
