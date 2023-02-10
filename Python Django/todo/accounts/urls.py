from django.urls import path

# IMPORT [views.py]
from . import views

# RENDER VIEWS
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup")
]