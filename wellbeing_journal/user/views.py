from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm


def home_page(request):
    return HttpResponse("<h1>Hello, it's a home page!</h1>")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

