from django.shortcuts import render, redirect, get_list_or_404

# LOGIN
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    return render(request, 'page/home.html')

def rules(request):
    return render(request, 'page/rules.html')

# LOGIN [LOGIN REQUEST]
@login_required
def wishLish(request):
    names_list = ['Wallace', 'Tony', 'Riri']
    return render(request, 'page/list.html', {'names':names_list})

@login_required
def dashboard(request):
    return render(request, 'page/dashboard.html')