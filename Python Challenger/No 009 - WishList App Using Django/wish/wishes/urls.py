from django.urls import path

# IMPORT [views.py]
from . import views

urlpatterns = [
    path('', views.homePage, name="página inicial"),
    path('rules/', views.rules, name="regras do projeto"),
    path('list/', views.wishList, name="lendo listagem"),
    path('list/new-wish/', views.createWish, name="criar"),
    path('list/update/<int:wish_id>', views.updateWish, name="atualizar"),
    path('list/delete/<int:wish_id>', views.deleteWish, name="apagar"),
    path('list/status/<int:wish_id>', views.statusWish, name="estado"),
    path('graph/', views.dashboard, name="dashboard"),
]