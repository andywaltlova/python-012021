from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from . import models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"


class CarsView(ListView):
    model = models.Car
    template_name = 'car_template.html'


class CarDetailView(DetailView):
    model = models.Car
    template_name = "car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered = models.LoanRecord.objects.filter(
            car=self.kwargs['pk']).count()
        context["num_of_loans"] = filtered
        return context


class CreateCar(CreateView):
    model = models.Car
    template_name = "create_car/create_car.html"
    fields = ["license_plate", "car_type", "mileage", "last_tech_inspection"]
    success_url = reverse_lazy('car_added')


class CarAdded(TemplateView):
    template_name = "create_car/ack_car.html"


class LoansView(ListView):
    model = models.LoanRecord
    template_name = 'loan_template.html'


class LoanDetailView(DetailView):
    model = models.LoanRecord
    template_name = "loan_detail.html"


class CreateLoan(CreateView):
    model = models.LoanRecord
    template_name = "create_loan/create_loan.html"
    fields = ["start", "end", "price", "car", "customer", "is_approved"]
    success_url = reverse_lazy('loan_added')


class LoanAdded(TemplateView):
    template_name = "create_loan/ack_loan.html"


class CustomerView(ListView):
    model = models.Customer
    template_name = 'customer_template.html'


class CustomerDetailView(DetailView):
    model = models.Customer
    template_name = "customer_detail.html"
