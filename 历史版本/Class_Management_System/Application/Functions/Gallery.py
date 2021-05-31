from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path


def gallery_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级Gallery"

    return render(request, 'Gallery.html', locals())