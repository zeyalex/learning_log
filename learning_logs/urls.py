"""Defines URL patterns for learning_logs"""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # головна сторінка
    path('', views.index, name='index'),
]