from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Daily
from .forms import CreateGratefulPost, CreateJournalingPost, AddDailyPic


today = datetime.today()


def instance_from_date(request, date):
    instance = Daily.objects.all().filter(author=request.user, date=date).first()
    return instance


def is_there_instance_already(request):
    instance = instance_from_date(request, today)
    if not instance:
        instance = Daily(author=request.user)
    return instance


def cleaned_data2list(form):
    list_ = []
    for key, value in form.cleaned_data.items():
        list_.append(value)
    return list_


def home_page(request):
    context = {
        'title': 'Home Page',
        'today_date': datetime.now().strftime("%d %b, %Y"),
        'today_weekday': datetime.now().strftime("%A"),
        }
    if request.user.is_authenticated:
        context.update({
                        'instance': instance_from_date(request, date=today),
                        'user_posts': Daily.objects.all().filter(author=request.user).order_by('-date'),
                        })

    return render(request, 'journal/home.html', context)


@login_required
def add_gratitude_post(request):
    instance = is_there_instance_already(request)
    if request.method == "POST":
        gratitude_form = CreateGratefulPost(request.POST)
        if gratitude_form.is_valid():
            instance.grateful_for = cleaned_data2list(gratitude_form)
            instance.save()
            return redirect('gratitude')
    if instance.grateful_for:
        grateful_for_list = instance.grateful_for
        g1, g2, g3 = grateful_for_list[0], grateful_for_list[1], grateful_for_list[2]
        gratitude_form = CreateGratefulPost(initial={'grateful_for1': g1, 'grateful_for2': g2, 'grateful_for3': g3})
    else:
        gratitude_form = CreateGratefulPost()
    return render(request, 'journal/gratitude_form.html',
                  {
                        'title': 'Gratitude Journal',
                        'today_weekday': datetime.now().strftime("%A"),
                        'gratitude_form': gratitude_form
                  })


@login_required
def gratitude(request):
    try:
        instance = instance_from_date(request, today)
        if instance.grateful_for:
            return render(request, 'journal/gratitude.html',
                          {
                                'title': 'Gratitude Journal',
                                'instance': instance
                          })
        else:
            return redirect('gratitude_form')
    except AttributeError:
        pass
        return redirect('gratitude_form')


@login_required
def delete_gratitude_post(request):
    instance = instance_from_date(request, today)
    instance.grateful_for = None
    instance.save()
    return redirect('gratitude_form')


@login_required
def add_journaling_post(request):
    instance = is_there_instance_already(request)
    if request.method == "POST":
        journaling_form = CreateJournalingPost(request.POST, instance=instance)
        if journaling_form.is_valid():
            instance.thoughts = journaling_form.cleaned_data.get("thoughts")
            instance.save()
            return redirect('journaling')
    else:
        journaling_form = CreateJournalingPost(instance=instance)
    return render(request, 'journal/journaling_form.html',
                  {
                      'title': 'Journal',
                      'today_date': datetime.now().strftime("%d %b, %Y"),
                      'journaling_form': journaling_form
                  })


@login_required
def journaling(request):
    try:
        instance = instance_from_date(request, today)
        if instance.thoughts is None:
            return redirect('journaling_form')
        else:
            return render(request, 'journal/journaling.html',
                          {
                              'title': 'Your thoughts',
                              'instance': instance
                          })
    except AttributeError:
        return redirect('journaling_form')


@login_required
def delete_journaling_post(request):
    try:
        instance = instance_from_date(request, today)
        instance.thoughts = None
        instance.save()
    except AttributeError:
        pass
    return redirect('journaling_form')


@login_required
def daily_pic(request):
    instance = is_there_instance_already(request)
    if request.method == "POST":
        daily_pic_form = AddDailyPic(request.POST, request.FILES, instance=instance)
        if daily_pic_form.is_valid():
            instance.daily_pic = daily_pic_form.cleaned_data.get('daily_pic')
            instance.save()
            return redirect('daily_pic')
    else:
        daily_pic_form = AddDailyPic(instance=instance)
    return render(request, 'journal/daily_pic.html',
                  {
                      'title': 'Photo Journal',
                      'daily_pic': daily_pic_form,
                      'instance': instance
                  })


@login_required
def delete_pic(request):
    try:
        instance = instance_from_date(request, today)
        instance.daily_pic.delete(save=True)
        instance.save()
    except AttributeError:
        pass
    return redirect('daily_pic')
