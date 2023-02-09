from django.urls import path

# IMPORT [views.py]
from . import views

# RENDER VIEWS
urlpatterns = [
    path('', views.homePage),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<int:task_id>', views.taskView, name="task-view-list"),
    path('task-list/new_task/', views.createTask, name="new-task"),
    path('task-list/edit/<int:task_id>', views.updateTask, name="edit-task"),
    path('task-list/delete/<int:task_id>', views.deleteTask, name="delete-task"),
    path('name/<str:name>', views.yourName)
]