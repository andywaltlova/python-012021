from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models


class IndexView(View):
    def get(self, request):
        return HttpResponse(
            """
    <h1 style='text-align:center'>Welcome to our car rental!</h1>
    <p style='text-align:center'><a href='http://localhost:8000/catalog/list/'>What cars do we have?</a><br></p>
    <h2 style='text-align:center'>About us</h2>
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