from django.urls import path

# IMPORT [views.py]
from . import views

# RENDER VIEWS
urlpatterns = [
    path('', views.taskList, name="task-list"),
    path('name/<str:name>', views.yourName)
]