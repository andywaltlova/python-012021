from django.urls import path

from . import views

urlpatterns = [
    path('', views.MySecondView.as_view(), name='index'),
]
