from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path


def message_homework_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 用于优化页面细节
    page = "通知&消息"
    path = get_image_path(student_num)

    # 查询所有有效作业通知
    messages = models.message_homework.objects.filter(useable=True).order_by("-published_time")

    # 查询未读作业通知，特殊显示
    unnoticed_homework = [message.ms_num_id for message in
                          models.notice_homework.objects.filter(student_num_id=student_num)]

    # 查询所有四种通知的未读消息个数，用于显示未读消息个数
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
    return render(request, "messages_homework.html", locals())


def message_competition_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "通知&消息"
    path = get_image_path(student_num)

    # 获取所有比赛通知
    messages = models.message_competition.objects.filter(useable=True).order_by("-published_time")

    # 查询所有四种通知的未读消息个数，用于显示未读消息个数
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))

    # 获取未读比赛通知列表，特殊显示
    unnoticed_messages = [message.ms_num_id for message in
                          models.notice_competition.objects.filter(student_num_id=student_num)]
    return render(request, "messages_competition.html", locals())


def message_activity_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "通知&消息"
    path = get_image_path(student_num)

    # 获取所有有效活动通知
    messages = models.message_activity.objects.filter(useable=True).order_by("-published_time")

    # 查询所有四种通知的未读消息个数，用于显示未读消息个数
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))

    # 获取所有未读消息列表，特殊显示
    unnoticed_messages = [message.ms_num_id for message in
                          models.notice_activity.objects.filter(student_num_id=student_num)]
    return render(request, "messages_activity.html", locals())


def message_message_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "通知&消息"
    path = get_image_path(student_num)

    # 获取所有未读消息
    messages = models.message_message.objects.filter(useable=True, target_student_num_id=student_num).order_by("-published_time")

    # 查询所有四种通知的未读消息个数，用于显示未读消息个数
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))

    # 获取未读消息列表，特殊显示
    unnoticed_messages = [message.ms_num_id for message in
                          models.notice_message.objects.filter(student_num_id=student_num)]
    return render(request, "messages_message.html", locals())


def detailed_message_page(request, upload_resault = "-1"):
    # 获取学生学号、姓名、auth
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "通知&消息"
    path = get_image_path(student_num)

    # 获取回传的ms_num(message_id)和通知种类
    message_id = request.GET.get("message_id")
    type_code = request.GET.get("type")

    # 根据通知种类返回页面
    if type_code == "0":
        # 在相应的数据库中查找通知详细内容，这里可能出现一个同学点击通知的时候通知被删除的情况，需要捕获错误（删除通知功能还未添加，如添加需要增加try..except...语句） 下同
        message = models.message_homework.objects.get(ms_num=message_id)

        # 查询相应notice表，如存在相关记录，则删除该记录，表示这条通知该同学已读 下同
        try:
            notice = models.notice_homework.objects.get(ms_num=message_id, student_num_id=student_num)
            notice.delete()
        except:
            pass
        return render(request, "homework_message.html", locals())
    elif type_code == "1":
        # 在相应的数据库中查找通知详细内容，这里可能出现一个同学点击通知的时候通知被删除的情况，需要捕获错误（删除通知功能还未添加，如添加需要增加try..except...语句） 下同
        message = models.message_competition.objects.get(ms_num=message_id)

        # 查询相应notice表，如存在相关记录，则删除该记录，表示这条通知该同学已读 下同
        try:
            notice = models.notice_competition.objects.get(ms_num=message_id, student_num_id=student_num)
            notice.delete()
        except:
            pass
        return render(request, "competition_message.html", locals())
    elif type_code == "2":
        # 在相应的数据库中查找通知详细内容，这里可能出现一个同学点击通知的时候通知被删除的情况，需要捕获错误（删除通知功能还未添加，如添加需要增加try..except...语句） 下同
        message = models.message_activity.objects.get(ms_num=message_id)

        # 查询相应notice表，如存在相关记录，则删除该记录，表示这条通知该同学已读 下同
        try:
            notice = models.notice_activity.objects.get(ms_num=message_id, student_num_id=student_num)
            notice.delete()
        except:
            pass
        return render(request, "activity_message.html", locals())
    elif type_code == "3":
        # 在相应的数据库中查找通知详细内容，这里可能出现一个同学点击通知的时候通知被删除的情况，需要捕获错误（删除通知功能还未添加，如添加需要增加try..except...语句） 下同
        message = models.message_message.objects.get(ms_num=message_id)
        try:
            notice = models.notice_message.objects.get(ms_num=message_id, student_num_id=student_num)
            notice.delete()
        except:
            pass
        send_person_name = models.student.objects.get(student_num_id=message.send_person_student_num_id).student_name
        return render(request, "message_message.html", locals())
    else:
        pass

    return render(request, "homework_message.html", locals())


def competition_publishment_page(request):
    # 传递学号、用户名和权限信息
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "班级管理"
    path = get_image_path(student_num)

    return render(request, "competition_upload.html", locals())


def activity_publishment_page(request):
    # 传递学号、用户名和权限信息
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "班级管理"
    path = get_image_path(student_num)

    return render(request, "activity_upload.html", locals())


def homework_publishment_page(request):
    # 传递学号、用户名和权限信息
    student_num = request.GET.get("student_num")
    student_name = models.student.objects.get(student_num=student_num).student_name
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "班级管理"
    path = get_image_path(student_num)

    return render(request, "homework_upload.html", locals())
