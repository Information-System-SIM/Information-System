from django.shortcuts import render

# Create your views here.
from Application import models


def index(request):
    return render(request, 'index.html')

def show_login(request):
    return render(request, 'pages-signin.html')

def login(request):
    if request.method == "GET":
        return render(request, "pages-signin.html")
    elif request.method == "POST":
        student_num_entered = str(request.POST["student_num"])
        password_entered = request.POST["password"]
        try:
            user_true = models.users.objects.get(student_num__exact=student_num_entered)
            password_true = user_true.pwd
            if password_true == password_entered:
                return render(request, "index.html")
            else:
                return render(request, "pages-signin.html", {"password_true": False})
        except:
            return render(request, "pages-signin.html", {"User_Exit":False})

def table(request):
    datas = models.users.objects.all()
    print("datas:")
    print(datas)
    return render(request, 'tables-basic.html', {"datas" : datas})

