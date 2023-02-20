from django.shortcuts import render, redirect, get_object_or_404

# LOGIN
from django.contrib.auth.decorators import login_required

# IMPORT[wishes]
from .models import Wish
from .forms import WishForm

# Create your views here.
def homePage(request):
    """
        Project home page
    """
    return render(request, 'page/home.html')

def rules(request):
    return render(request, 'page/rules.html')

# LOGIN [LOGIN REQUEST]
@login_required
def wishList(request):
    """
        Reading the database
        ├── Args:
            └── request : Important Django requirement

        ├── Return:
            ├── wish_list : All database values sorted in order of creation
    """

    wish_list = Wish.objects.all().order_by('-created_at')
    return render(request, 'page/list.html', {'wishes':wish_list})

@login_required
def createWish(request):
    """
        Create a new wish.
        ├── Args:
            └── request : Important Django requirement

        ├── Return:
            ├── wish_list : All database values sorted in order of creation
            └── form : create form
    """

    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.done = 'adn'
            wish.user = request.user
            wish.save()

            return redirect('/list/')

    else:
        form = WishForm()
        return render(request, 'page/create.html', {'form':form})

@login_required
def updateWish(request, wish_id):
    """
        Update selected wish
        ├── Args:
            ├── request : Important Django requirement
            └── wish_id : Wish's ID

        ├── Return:
            ├── wish : Get selected wish data
            └── form : update form
    """
    wish = get_object_or_404(Wish, pk=wish_id)
    form = WishForm(instance=wish)

    if request.method == 'POST':
        form = WishForm(request.POST, instance=wish)

        if form.is_valid():
            wish.save()
            return redirect('/list/')

    else:
        content = {'form':form, 'wish':wish}
        return render(request, 'page/edit.html', content)

@login_required
def deleteWish(request, wish_id):
    """
        Delete selected wish
        ├── Args:
            ├── request : Important Django requirement
            └── wish_id : Wish's ID

        ├── Return:
            ├── wish : Get selected wish data
    """
    wish = get_object_or_404(Wish, pk=wish_id)
    wish.delete()
    return redirect('/list/')

@login_required
def statusWish(request, wish_id):
    """
        Change wish status
        ├── Args:
            ├── request : Important Django requirement
            └── wish_id : Wish's ID

        ├── Return:
            ├── wish : Get selected wish data
    """
    
    wish = get_object_or_404(Wish, pk=wish_id)

    if (wish.done == 'adn'):
        wish.done = 'rld'

    else:
        wish.done = 'adn'

    wish.save()
    return redirect('/list/')

@login_required
def dashboard(request):
    return render(request, 'page/dashboard.html')