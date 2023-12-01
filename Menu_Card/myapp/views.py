from django.shortcuts import render,HttpResponse
from Menu_Card import urls

def index(request):
    return render(request,"index.html")
def add_menu(request):
    return render(request,"add_menu.html")

# Create your views here.
