from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Application import models
from Application.Functions import Login, Document_Management
from Class_Management_System import settings
import os


# Create your views here.


def mainpage(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth
        student = models.student.objects.get(student_num=student_num)
        student_name = student.student_name
        self_description = student.self_description
        return render(request, 'mainpage.html',locals())
    else:
        pass


def show_login(request):
    return render(request, 'pages-signin.html')


def login(request):
    if request.method == "GET":
        return render(request, "pages-signin.html")
    elif request.method == "POST":
        return Login.login(request)


def table(request):
    datas = models.users.objects.all()
    print("datas:")
    print(datas)
    return render(request, 'tables-basic.html', {"datas": datas})


def change_password(request):
    if request.method == "GET":
        return render(request, "pages-changeid.html")
    elif request.method == "POST":
        return Login.change_password(request)


def homework_upload(request):
    if request.method == "get":
        student_num = request.GET.get("student_num")
        homework_name = request.GET.get("homework_name")
        return render(request, "document_upload.html", {"student_num":student_num,"homework_name":homework_name})
    elif request.method == "POST":
        student_num = request.POST["student_num"]
        homework_name = request.POST["homework_name"]
        Document_Management.homework_upload(request, student_num, homework_name)
        return render(request, "document_upload.html")
    else:
        student_num = request.GET.get("student_num")
        homework_name = request.GET.get("homework_name")
        return render(request, "document_upload.html", {"student_num":student_num,"homework_name":homework_name})

def message(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        messages = models.message_homework.objects.filter(useable=True)
        unnoticed_messages = [message.ms_num_id for message in models.notice_homework.objects.filter(student_num_id=student_num)]
        return render(request, "messages_homework.html", locals())