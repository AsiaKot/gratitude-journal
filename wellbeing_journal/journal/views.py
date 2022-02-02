from django.shortcuts import render


def home_page(request):
    return render(request, 'journal/home.html')


def gratitude(request):
    return render(request, 'journal/gratitude.html')


def journaling(request):
    return render(request, 'journal/journaling.html')
