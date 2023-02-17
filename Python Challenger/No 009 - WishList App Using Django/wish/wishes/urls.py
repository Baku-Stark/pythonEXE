from django.contrib import admin
from django.urls import path

# IMPORT [views.py]
from . import views

urlpatterns = [
    path('', views.homePage, name="página inicial"),
    path('list/', views.wishLish, name="listagem")
]