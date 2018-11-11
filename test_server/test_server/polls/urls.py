from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
]
