from django.urls import path

from . import views

urlpatterns = [
    path('', views.MyFirstView.as_view(), name='index'),
]
