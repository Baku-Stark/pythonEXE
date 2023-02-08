from django.urls import path

# IMPORT [views.py]
from . import views

# RENDER VIEWS
urlpatterns = [
    path('', views.homePage),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<int:task_id>', views.taskView, name="task-view-list"),
    path('name/<str:name>', views.yourName)
]