# hello_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_hello_message, name='hello_message'),
]
