
from django.urls import path
from . import views

#define a list of url patterns


urlpatterns = [
    path('', views.index),
]

