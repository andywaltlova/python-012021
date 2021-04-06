from django.urls import path

from . import views

urlpatterns = [
    path('', views.MujPrvniPohled.as_view(), name='index'),
]
