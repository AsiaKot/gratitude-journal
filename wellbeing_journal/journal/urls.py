from django.urls import path
from . import views as journal_views
from .views import GratitudePostListView, GratitudePostCreateView


urlpatterns = [
    path('', journal_views.home_page, name='home_page'),
    path('gratitude/', GratitudePostListView.as_view(), name='gratitude'),
    path('gratitude/new', GratitudePostCreateView.as_view(), name='gratitude_form'),
    path('journaling/', journal_views.journaling, name='journaling')
]
