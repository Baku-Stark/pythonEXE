from django.urls import path

# IMPORT [views.py]
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup")
]