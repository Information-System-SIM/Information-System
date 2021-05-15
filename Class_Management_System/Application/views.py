from django.shortcuts import render

# Create your views here.
from Application import models


def index(request):
    return render(request, 'index.html')

def show_login(request):
    return render(request, 'pages-signin.html')

def login(request):
    username = request.POST['username']
    pwd = request.POST['pwd']
    print(username + pwd)

def table(request):
    datas = models.users.objects.all()
    print("datas:")
    print(datas)
    return render(request, 'tables-basic.html', {"datas" : datas})

