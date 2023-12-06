from django.shortcuts import render,HttpResponse
from Menu_Card import urls
from .forms import MenuForm
from .models import MenuUpload

def index(request):
    menu =MenuUpload.objects.all()
    return render(request,"index.html",{'menu':menu})



def add_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    form = MenuForm()
    return render(request,"add_menu.html",{'form':form})


def admin_home(request):
    return render(request,"admin_home.html")

def admin_login(request):
    return render(request,"adminlogin.html")

# Create your views here.
