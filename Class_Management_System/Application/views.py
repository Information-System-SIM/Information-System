from random import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Application import models
from Application.Functions import Login, Document_Management
from Class_Management_System import settings
from Application.Functions.function import transfer
import os
import datetime

# Create your views here.
from Class_Management_System.settings import BASE_DIR


def mainpage(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth
        student = models.student.objects.get(student_num=student_num)
        student_name = student.student_name
        self_description = student.self_description
        path = "Image/" + student_num + ".jpeg"
        course_path = "Image/course.png"
        unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
        unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
        unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
        unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
        message_num = unnoticed_homework_num + unnoticed_competition_num + unnoticed_activity_num + unnoticed_message_num
        print(message_num)
        return render(request, 'mainpage.html', locals())
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
        return render(request, "document_upload.html", {"student_num": student_num, "homework_name": homework_name})
    elif request.method == "POST":
        student_num = request.POST["student_num"]
        homework_name = request.POST["homework_name"]
        Document_Management.homework_upload(request, student_num, homework_name)
        return render(request, "document_upload.html")
    else:
        student_num = request.GET.get("student_num")
        homework_name = request.GET.get("homework_name")
        return render(request, "document_upload.html", {"student_num": student_num, "homework_name": homework_name})


# 作业通知
def message_homework(request):
    if request.method == "GET":
        page = "通知&消息"
        student_num = request.GET.get("student_num")
        messages = models.message_homework.objects.filter(useable=True)
        unnoticed_homework = [message.ms_num_id for message in
                              models.notice_homework.objects.filter(student_num_id=student_num)]
        unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
        unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
        unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
        unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
        return render(request, "messages_homework.html", locals())


# 比赛通知
def message_competition(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        messages = models.message_competition.objects.filter(useable=True)
        unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
        unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
        unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
        unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
        unnoticed_messages = [message.ms_num_id for message in
                              models.notice_competition.objects.filter(student_num_id=student_num)]
        return render(request, "messages_competition.html", locals())


# 活动通知
def message_activity(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        messages = models.message_activity.objects.filter(useable=True)
        unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
        unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
        unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
        unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
        unnoticed_messages = [message.ms_num_id for message in
                              models.notice_activity.objects.filter(student_num_id=student_num)]
        return render(request, "messages_activity.html", locals())


# 通知消息
def message_message(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num)
        messages = models.message_message.objects.filter(useable=True)
        unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
        unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
        unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
        unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
        unnoticed_messages = [message.ms_num_id for message in
                              models.notice_message.objects.filter(student_num_id=student_num)]
        return render(request, "messages_message.html", locals())


# 查看消息详情
def message(request):
    if request.method == "GET":
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth
        # 根据传回的message_id获取到唯一对应的通知
        message_id = request.GET.get("message_id")
        type_code = request.GET.get("type")
        if type_code == "0":
            message = models.message_homework.objects.get(ms_num=message_id)
            try:
                notice = models.notice_homework.objects.get(ms_num=message_id,student_num_id=student_num)
                notice.delete()
            except:
                pass
            return render(request, "homework_message.html", locals())
        elif type_code == "1":
            message = models.message_competition.objects.get(ms_num=message_id)
            try:
                notice = models.notice_competition.objects.get(ms_num=message_id,student_num_id=student_num)
                notice.delete()
            except:
                pass
            return render(request, "competition_message.html", locals())
        elif type_code == "2":
            message = models.message_activity.objects.get(ms_num=message_id)
            try:
                notice = models.notice_activity.objects.get(ms_num=message_id,student_num_id=student_num)
                notice.delete()
            except:
                pass
            return render(request, "activity_message.html", locals())
        elif type_code == "3":
            message = models.message_message.objects.get(ms_num=message_id)
        else:
            return render(request, "competition_message.html", {"Not_Exist":True})

        return render(request, "competition_message.html", locals())


def competition_publishment(request):
    if request.method == "GET":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        return render(request, "competition_upload.html", locals())
    elif request.method == "POST":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        # 获取表单信息
        title = request.POST["competition_title"]
        description = request.POST["description"]
        competition_date = request.POST["competition_date"]
        competition_time = request.POST["competition_time"]
        place = request.POST["place"]

        # 转换比赛日期时间为可写入数据库的格式
        competition_datetime = transfer(competition_date,competition_time)

        # 将比赛信息写入数据库
        ms_num = models.message_competition.objects.create(title=title,description=description,competition_time=competition_datetime,place=place,useable=True).ms_num

        # 将比赛未读信息写入数据库
        stu_lst = [stu.student_num for stu in models.users.objects.all()]
        for stu_num in stu_lst:
            models.notice_competition.objects.create(ms_num_id=ms_num,student_num_id=stu_num)

        return render(request, "competition_upload.html", {"student_num":student_num, "auth":auth})


def activity_publishment(request):
    if request.method == "GET":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        return render(request, "activity_upload.html", locals())
    elif request.method == "POST":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        # 获取表单信息
        title = request.POST["activity_title"]
        description = request.POST["description"]
        activity_date = request.POST["activity_date"]
        activity_time = request.POST["activity_time"]
        place = request.POST["place"]

        # 转换比赛日期时间为可写入数据库的格式
        activity_datetime = transfer(activity_date, activity_time)

        # 将比赛信息写入数据库
        ms_num = models.message_activity.objects.create(title=title, description=description,
                                                           activity_time=activity_datetime, place=place,
                                                           useable=True).ms_num

        # 将比赛未读信息写入数据库
        stu_lst = [stu.student_num for stu in models.users.objects.all()]
        for stu_num in stu_lst:
            models.notice_activity.objects.create(ms_num_id=ms_num, student_num_id=stu_num)

        return render(request, "activity_upload.html", {"student_num": student_num, "auth": auth})

def homework_publishment(request):
    if request.method == "GET":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        return render(request, "homework_upload.html", locals())
    elif request.method == "POST":

        # 传递用户名和权限信息
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        # 获取表单信息
        title = request.POST["homework_title"]
        text = request.POST["text"]
        homework_date = request.POST["homework_date"]
        homework_time = request.POST["homework_time"]
        subject = request.POST["subject"]
        requirement = request.POST["requirement"]

        # 转换比赛日期时间为可写入数据库的格式
        deadline_datetime = transfer(homework_date, homework_time)

        # 将比赛信息写入数据库
        ms_num = models.message_homework.objects.create(title=title, text = text, Requirement=requirement, subject=subject, deadline=deadline_datetime, useable=True).ms_num

        # 将比赛未读信息写入数据库
        stu_lst = [stu.student_num for stu in models.users.objects.all()]
        for stu_num in stu_lst:
            models.notice_homework.objects.create(ms_num_id=ms_num, student_num_id=stu_num)

        return render(request, "homework_upload.html", {"student_num": student_num, "auth": auth})