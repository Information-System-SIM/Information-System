from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path

def mainpage_show(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth
    student = models.student.objects.get(student_num=student_num)
    student_name = student.student_name
    self_description = student.self_description
    path = get_image_path(student_num)
    unnoticed_homework_num = len(models.notice_homework.objects.filter(student_num_id=student_num))
    unnoticed_competition_num = len(models.notice_competition.objects.filter(student_num_id=student_num))
    unnoticed_activity_num = len(models.notice_activity.objects.filter(student_num_id=student_num))
    unnoticed_message_num = len(models.notice_message.objects.filter(student_num_id=student_num))
    message_num = unnoticed_homework_num + unnoticed_competition_num + unnoticed_activity_num + unnoticed_message_num
    print(message_num)
    return render(request, 'mainpage.html', locals())