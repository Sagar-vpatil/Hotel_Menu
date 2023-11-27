from django.shortcuts import render,HttpResponse
from Menu_Card import urls

def index(request):
    return render(request,"index.html")

# Create your views here.
