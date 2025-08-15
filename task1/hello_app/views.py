from django.shortcuts import render
from django.http import HttpResponse


def show_hello_message(request):
    # نام خود را اینجا وارد کنید
    your_name = "Ali Heidari"
    return HttpResponse(f"Hello World {your_name}")
