from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Application import models

# Create your views here.

def index(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth
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
                return HttpResponseRedirect(redirect_to="/index?student_num="+user_true.student_num)
            else:
                return render(request, "pages-signin.html", {"password_true": False})
        except:
            return render(request, "pages-signin.html", {"User_Exit":False})

def table(request):
    datas = models.users.objects.all()
    print("datas:")
    print(datas)
    return render(request, 'tables-basic.html', {"datas" : datas})

def change_password(request):
    if request.method == "GET":
        return render(request, "pages-changeid.html")
    elif request.method == "POST":
        student_num = request.POST["student_num"]
        origin_password = request.POST["origin_password"]
        new_password = request.POST["pwd"]
        new_password_confirm = request.POST["pwd_confirm"]
        try:
            user = models.users.objects.get(student_num=student_num)
            origin_password_right = user.pwd
            print(0)
            if origin_password_right == origin_password:
                if new_password == new_password_confirm:
                    user.pwd = new_password
                    user.save()
                    print(1) #test
                    return render(request, "pages-changeid.html", {"confirmation":True})
                else:
                    print(2) #test
                    return render(request, "pages-changeid.html", {"confirmation":False})
            else:
                print(3) #test
                return render(request, "pages-changeid.html", {"origin_pwd_right": False})
        except:
            print(4) #test
            return render(request, "pages-changeid.html", {"studentnum_exist":False})