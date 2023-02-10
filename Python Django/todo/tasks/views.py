from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# PAGINAÇÃO
from django.core.paginator import Paginator

# [MODELS]
from .models import Task
from .forms import TaskForm

# Create your views here.
def homePage(request):
    return render(request, 'tasks/home.html')

# RENDERIZAR O PRIMEIRO ARQUIVO HTML
# LISTA DE TAREFAS [arquivo principal]
@login_required
def taskList(request):
    # request.GET.get(<name="search">)
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

        if search != tasks:
            return render(request, 'tasks/no-item.html')
        
    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

        return render(request, 'tasks/list.html', {'tasks' : tasks})

# RENDERIZAR UMA VARIÁVEL
@login_required
def yourName(request, name):
    return render(request, 'tasks/name.html', {'name': name})

# RENDERIZAR AS TAREFAS
@login_required
def taskView(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task.html', {'task' : task})

# CRIAR NOVA TAREFA
@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/task-list/')


    else:
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form' : form})

# ATUALIZAR UMA TAREFA
@login_required
def updateTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/task-list/')
    
    else:
        return render(request, 'tasks/edit.html', {'form' : form, 'task' : task})

# APAGAR TAREFA
@login_required
def deleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/task-list/')