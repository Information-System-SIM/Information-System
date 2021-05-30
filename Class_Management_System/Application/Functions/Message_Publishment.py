import os
from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path
from Class_Management_System.settings import BASE_DIR
from django.contrib import messages


def message_notice(request):
    messages.success(request,"通知发布成功")


def transfer(date_str,time_str):
    lst = str(date_str).split("/")
    time_lst = str(time_str).split(":")
    result = lst[-1] + "-" + lst[0] + "-" + lst[1] + " " + time_lst[0] + ":" + time_lst[1] + ":00"
    return result


def competition_publishment_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    auth = request.session["auth"]

    # 获取表单信息
    title = request.POST["competition_title"]
    description = request.POST["description"]
    competition_date = request.POST["competition_date"]
    competition_time = request.POST["competition_time"]
    place = request.POST["place"]

    # 转换比赛日期时间为可写入数据库的格式
    competition_datetime = transfer(competition_date, competition_time)

    # 将比赛信息写入数据库
    ms_num = models.message_competition.objects.create(title=title, description=description,
                                                       competition_time=competition_datetime, place=place,
                                                       useable=True).ms_num

    # 将比赛未读信息写入数据库
    stu_lst = [stu.student_num for stu in models.users.objects.all()]
    for stu_num in stu_lst:
        models.notice_competition.objects.create(ms_num_id=ms_num, student_num_id=stu_num)

    message_notice(request)
    return render(request, "competition_upload.html", {"student_num": student_num, "auth": auth})


def activity_publishment_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

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

    message_notice(request)
    return render(request, "activity_upload.html", locals())


def homework_publishment_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

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
    ms_num = models.message_homework.objects.create(title=title, text=text, Requirement=requirement, subject=subject,
                                                    deadline=deadline_datetime, useable=True).ms_num

    # 将比赛未读信息写入数据库
    stu_lst = [stu.student_num for stu in models.users.objects.all()]
    for stu_num in stu_lst:
        models.notice_homework.objects.create(ms_num_id=ms_num, student_num_id=stu_num)

    path = os.path.join(BASE_DIR,'static/Documents/'+str(ms_num))
    os.mkdir(path)

    message_notice(request)
    return render(request, "homework_upload.html", locals())