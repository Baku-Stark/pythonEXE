from django.urls import path

# IMPORT [views.py]
# http://127.0.0.1:8000/helloworld/
from . import views

# IMPORT [views CRUD]


# Rendering HTML pages
urlpatterns = [
    path('', views.wishList, name='wish-list'),
]