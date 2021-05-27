import os

import django.core.files

from Application import models
from Class_Management_System.settings import BASE_DIR


# 文件管理模块


# 传入参数request，学号和作业名，可以直接将上传文件存储
def homework_upload(request, student_num, message_id):
    if request.FILES:
        file = request.FILES.get('document', None)
        file_format = file.name.split(".")[1]
        homework_name = models.message_homework.objects.get(ms_num=message_id).title
        file_name = str(student_num) + "_" + str(homework_name) + "." + file_format
        path = os.path.join(BASE_DIR, 'static/Documents/' + str(message_id) + "/")
        with open(path + file_name, "wb+") as f:
            for chunk in file:
                f.write(chunk)
        try:
            origin_record = models.homework_upload.objects.get(student_num_id=student_num,ms_num_id=message_id)
            origin_record.delete()
        except:
            pass
        models.homework_upload.objects.create(ms_num_id=message_id,student_num_id=student_num,location=(path + file_name))
        return True
    else:
        return False
