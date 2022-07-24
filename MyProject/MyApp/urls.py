
from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("reservation", views.reservation, name='reservation'),


]
