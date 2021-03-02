"""Определяет схемы URL для learning_logs."""
from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    ]