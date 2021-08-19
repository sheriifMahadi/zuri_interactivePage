"""Defines URL patterns for backend_resume"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
]
