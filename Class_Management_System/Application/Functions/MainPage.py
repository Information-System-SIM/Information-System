from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path


# 主页函数
def mainpage_show(request):
    # 优化页面细节需要的参数，将必要渲染用参数存入session
    student_num = request.session["student_num"]
    auth = request.session["auth"]
    path = get_image_path(student_num)
    request.session["path"] = path
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
    message_num = unnoticed_homework_num + unnoticed_competition_num + unnoticed_activity_num + unnoticed_message_num
    message_notice_num = message_num - unnoticed_message_num
    request.session["message_num"] = message_num

    # 获取学生的信息
    student = models.student.objects.get(student_num=student_num)
    student_name = student.student_name
    request.session["student_name"] = student_name
    self_description = student.self_description

    return render(request, 'mainpage.html', locals())
