from django.http import HttpResponse
from django.template import loader

# IMPORT [models]
from .models import Wish
from .forms import WishForm

# IMPORT [db_functions]
from .db_functions import readWish
print(readWish())

# Main Page
def wishList(request):
    wish = Wish.objects.all().values()
    template = loader.get_template('pages/index.html')
    params = {'wishes': wish}
    print('oiiiiiiiiii')
    return HttpResponse(template.render(params, request))

# ----------------------------------
def Search(request, text):
    wish = Wish.objects.filter()

def CreateWish(request):
    form = WishForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('WishList')