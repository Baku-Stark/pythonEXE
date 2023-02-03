from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse


def  helloWorld(request):
    return HttpResponse('Hello World! s2')

def wishList(request):
    return render(request, 'pages/index.html')