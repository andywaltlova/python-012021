from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cars/', views.CarsView.as_view(), name='cars'),
    path('cars/<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
    path('loans/', views.LoansView.as_view(), name='loans'),
    path('loans/<int:pk>', views.LoanDetailView.as_view(), name='loan_detail'),
    path('customers/', views.CustomerView.as_view(), name='customers'),
    path('customers/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('cars/add/', views.CreateCar.as_view(), name='create_car'),
    path('cars/added/', views.CarAdded.as_view(),
         name='car_added'),
    path('loans/add/', views.CreateLoan.as_view(), name='create_loan'),
    path('loans/added/', views.LoanAdded.as_view(),
         name='loan_added'),
]
