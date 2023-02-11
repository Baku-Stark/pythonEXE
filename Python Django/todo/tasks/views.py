from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# PAGINAÇÃO
from datetime import datetime, timedelta
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

    # request.GET.get(<name="filter">)
    filter_status = request.GET.get('filter')
    # Filtrando as tarefas por status
    tasksDoneRecently = Task.objects.filter(done='done', update_at__gt=datetime.now()-timedelta(days=30)).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
        

    elif filter_status:
        tasks = Task.objects.filter(done=filter_status, user=request.user)

    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks' : tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})

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

# ALTERAR SITUAÇÃO DA TAREFA
@login_required
def changeTaskStatus(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/task-list/')