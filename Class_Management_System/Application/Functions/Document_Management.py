import os

import django.core.files

from Class_Management_System.settings import BASE_DIR


# 文件管理模块


# 传入参数request，学号和作业名，可以直接将上传文件存储
def homework_upload(request, student_num, homework_name):
    file = request.FILES.get('document')
    file_format = file.name.split(".")[1]
    file_name = str(student_num) + str(homework_name) + file_format
    path = os.path.join(BASE_DIR, 'static/Documents/' + str(homework_name) + "/")
    with open(path + file_name + file.name, "wb+") as f:
        for chunk in file:
            f.write(chunk)
