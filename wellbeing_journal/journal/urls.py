from django.urls import path
from . import views as journal_views


urlpatterns = [
    path('', journal_views.home_page, name='home_page'),
    path('gratitude/', journal_views.gratitude, name='gratitude'),
    path('journaling/', journal_views.journaling, name='journaling')
]
