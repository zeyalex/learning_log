"""Визначає регулярні вирази URL для learning_logs"""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # головна сторінка
    path('', views.index, name='index'),
    # Сторінка що відображає всі теми.
    path('topics/', views.topics, name='topics'),
    # Сторінка, присвячена окремій темі.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]