from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cars/', views.CarsView.as_view(), name='cars'),
    path('loans/', views.LoansView.as_view(), name='loans'),
    path('customers/', views.CustomerView.as_view(), name='customers')

]
