from django.shortcuts import render
from .models import Daily
from django.views.generic import ListView, CreateView
from datetime import datetime


def home_page(request):
    today_date = datetime.now().strftime("%d %b, %Y")
    today_weekday = datetime.now().strftime("%A")
    return render(request, 'journal/home.html',
                  {'title': 'Home Page', 'today_date': today_date, 'today_weekday': today_weekday})


def gratitude(request):
    return render(request, 'journal/gratitude.html', {'title': 'Gratitude Journal', 'gratitude_posts': Daily.objects.all()})


def journaling(request):
    return render(request, 'journal/journaling.html', {'title': 'Your thoughts'})


class GratitudePostListView(ListView):
    model = Daily
    template_name = 'journal/gratitude.html'
    context_object_name = 'gratitude_posts'


class GratitudePostCreateView(CreateView):
    model = Daily
    template_name = 'journal/gratitude_form.html'
    fields = ['grateful_for1', 'grateful_for2', 'grateful_for3']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

