from django.urls import path
from . import views as journal_views


urlpatterns = [
    path('', journal_views.home_page, name='home_page'),
    path('gratitude/', journal_views.gratitude, name='gratitude'),
    path('gratitude/add', journal_views.add_gratitude_post, name='gratitude_form'),
    path('gratitude/delete', journal_views.delete_gratitude_post, name='delete_gratitude_post'),
    path('journaling/', journal_views.journaling, name='journaling'),
    path('journaling/add', journal_views.add_journaling_post, name='journaling_form'),
    path('journaling/delete', journal_views.delete_journaling_post, name='delete_journaling_post')
]
