from django.shortcuts import render,HttpResponse
from Menu_Card import urls

def index(request):
    return render(request,"index.html")



def add_menu(request):
    return render(request,"add_menu.html")


def admin_home(request):
    return render(request,"admin_home.html")

def admin_login(request):
    return render(request,"adminlogin.html")

# Create your views here.
