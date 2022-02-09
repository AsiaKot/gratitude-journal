from django.shortcuts import render, redirect
from .models import Daily
from .forms import CreateGratefulPost, CreateJournalingPost
from datetime import datetime

today = datetime.today()


def home_page(request):
    today_date = datetime.now().strftime("%d %b, %Y")
    today_weekday = datetime.now().strftime("%A")
    instance = instance_from_date(request, today)
    return render(request, 'journal/home.html',
                  {
                        'title': 'Home Page',
                        'today_date': today_date,
                        'today_weekday': today_weekday,
                        'instance': instance
                   })


def instance_from_date(request, date):
    instance = Daily.objects.all().filter(author=request.user, date=date).first()
    return instance


def is_there_instance_already(request):
    instance = instance_from_date(request, today)
    if not instance:
        instance = Daily()
    else:
        pass
    return instance


def cleaned_data2list(form):
    gratitude_list = []
    for key, value in form.cleaned_data.items():
        val = value
        gratitude_list.append(val)
    return gratitude_list


def add_gratitude_post(request):
    if request.method == "POST":
        instance = is_there_instance_already(request)
        gratitude_form = CreateGratefulPost(request.POST)
        if gratitude_form.is_valid():
            instance.grateful_for = cleaned_data2list(gratitude_form)
            instance.save()
            return redirect('gratitude')
    else:
        gratitude_form = CreateGratefulPost()
    return render(request, 'journal/gratitude_form.html',
                  {
                        'title': 'Gratitude Journal',
                        'gratitude_form': gratitude_form
                  })


def delete_gratitude_post(request):
    instance = instance_from_date(request, today)
    instance.grateful_for = None
    instance.save()
    return redirect('gratitude_form')


def gratitude(request):
    try:
        instance = instance_from_date(request, today)
        gratitude_posts = instance.grateful_for
        if gratitude_posts:
            return render(request, 'journal/gratitude.html',
                          {
                                'title': 'Gratitude Journal',
                                'instance': instance
                          })
        else:
            return redirect('gratitude_form')
    except AttributeError:
        return redirect('gratitude_form')


def add_journaling_post(request):
    if request.method == "POST":
        instance = is_there_instance_already(request)
        journaling_form = CreateJournalingPost(request.POST, request.FILES)
        if journaling_form.is_valid():
            instance.thoughts = journaling_form.cleaned_data.get("thoughts")
            instance.daily_pic = journaling_form.cleaned_data.get("daily_pic")
            instance.save()
            return redirect('journaling')
    else:
        journaling_form = CreateJournalingPost()
    return render(request, 'journal/journaling_form.html',
                  {
                      'title': 'Journal',
                      'journaling_form': journaling_form
                  })


def delete_journaling_post(request):
    instance = instance_from_date(request, today)
    instance.thoughts = None
    instance.daily_pic.delete(save=True)
    instance.save()
    return redirect('journaling_form')


def journaling(request):
    try:
        instance = instance_from_date(request, today)
        thoughts = instance.thoughts
        if thoughts is None:
            return redirect('journaling_form')
        else:
            return render(request, 'journal/journaling.html',
                          {
                              'title': 'Your thoughts',
                              'instance': instance
                          })
    except AttributeError:
        return redirect('journaling_form')
