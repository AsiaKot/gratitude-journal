from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse("<h1>Welcome, it's a home page!</h1>")
