from django.urls import path

# IMPORT [views.py]
from . import views

urlpatterns = [
    path('', views.homePage, name="página inicial"),
    path('rules/', views.rules, name="regras do projeto"),
    path('list/', views.wishLish, name="listagem"),
    path('graph/', views.dashboard, name="dashboard"),
]