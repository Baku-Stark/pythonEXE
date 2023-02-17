from django.shortcuts import render, redirect, get_list_or_404

# Create your views here.
def homePage(request):
    return render(request, 'page/home.html')

def wishLish(request):
    names_list = ['Wallace', 'Tony', 'Riri']
    return render(request, 'page/list.html', {'names':names_list})