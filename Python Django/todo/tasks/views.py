from django.shortcuts import render, redirect, get_object_or_404

# [MODELS]
from .models import Task
from .forms import TaskForm

# Create your views here.
def homePage(request):
    return render(request, 'tasks/home.html')

# RENDERIZAR O PRIMEIRO ARQUIVO HTML
# LISTA DE TAREFAS [arquivo principal]
def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks' : tasks})

# RENDERIZAR UMA VARIÁVEL
def yourName(request, name):
    return render(request, 'tasks/name.html', {'name': name})

# RENDERIZAR AS TAREFAS
def taskView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task.html', {'task' : task})

# CRIAR NOVA TAREFA
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/task-list/')


    else:
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form' : form})