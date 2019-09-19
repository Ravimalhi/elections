from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import Polls, Cast, Result

urlpatterns = [
    path('polls', views.Polls, name='home'),
    path('cast', views.Cast, name='cast'),
    path('result', views.Result, name='result'),
   ]