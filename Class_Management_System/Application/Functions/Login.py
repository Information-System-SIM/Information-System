from django.http import HttpResponseRedirect
from django.shortcuts import render
from Application import models


# 登陆模块（包括用户名密码验证模块 和 更改密码模块）
def login(request):
    # 从表单中获取用户输入的用户名和密码
    student_num_entered = str(request.POST["student_num"])
    password_entered = request.POST["password"]

    # 从数据库读取真实的用户名和密码（根据用户名查找），若不存在会报错
    try:
        user_true = models.users.objects.get(student_num__exact=student_num_entered)
        password_true = user_true.pwd

        # 若用户名密码正确，重定向到主界面；否则返回密码错误
        if password_true == password_entered:
            request.session["student_num"] = student_num_entered
            request.session["auth"] = user_true.auth
            return HttpResponseRedirect(redirect_to="/mainpage?student_num=" + user_true.student_num)
        else:
            return render(request, "pages-signin.html", {"password_true": False})

    # 若用户名不存在则做出相应解释
    except:
        return render(request, "pages-signin.html", {"User_Exit": False})


def change_password(request):
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
                return HttpResponseRedirect("/login/")
            else:
                return render(request, "pages-changeid.html", {"confirmation": False})
        else:
            return render(request, "pages-changeid.html", {"origin_pwd_right": False})
    except:
        return render(request, "pages-changeid.html", {"studentnum_exist": False})
