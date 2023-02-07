from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return render(request, 'tasks/home.html')

# RENDERIZAR O PRIMEIRO ARQUIVO HTML
# LISTA DE TAREFAS [arquivo principal]
def taskList(request):
    return render(request, 'tasks/list.html')

# RENDERIZAR UMA VARIÁVEL
def yourName(request, name):
    return render(request, 'tasks/name.html', {'name': name})