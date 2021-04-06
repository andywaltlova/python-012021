from django.urls import path

from . import views

urlpatterns = [
    path('', views.MujDruhyPohled.as_view(), name='index'),
]
