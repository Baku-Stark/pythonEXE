from django.urls import path

# IMPORT [views.py]
# http://127.0.0.1:8000/helloworld/
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
]