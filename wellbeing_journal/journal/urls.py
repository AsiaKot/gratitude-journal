from django.urls import path
from . import views as journal_views


urlpatterns = [
    path('', journal_views.home_page, name='home_page')
]
