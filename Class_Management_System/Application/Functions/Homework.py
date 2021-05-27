import os
from urllib.parse import quote

from django.http import FileResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Application import models
from Application.Functions.function import get_image_path
from Class_Management_System.settings import BASE_DIR
import tkinter.messagebox as ms


def homework_page(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth

    # 优化页面细节
    page = "提交作业"
    path = get_image_path(student_num)

    uploaded_msnum = [x.ms_num_id for x in models.homework_upload.objects.filter(student_num_id=student_num)]
    homework_list = [[x.deadline, x.title, x.subject, x.text, x.ms_num] for x in
                     models.message_homework.objects.filter(useable=True).order_by("-deadline") if
                     x.ms_num in uploaded_msnum]

    return render(request, "uploaded_homework.html", locals())


def uploaded_homework_deal(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth
    ms_num = request.GET.get("message_id")
    order = request.GET.get("order")
    if order == "download":
        return download(student_num,ms_num)
    elif order == "delete":
        delete(student_num,ms_num)
        return homework_page(request)


def delete(student_num,ms_num):
    path = models.homework_upload.objects.get(ms_num_id=ms_num,student_num_id=student_num).location
    os.remove(path)
    models.homework_upload.objects.get(student_num_id=student_num,ms_num_id=ms_num).delete()


def download(student_num,ms_num):
    path = models.homework_upload.objects.get(ms_num_id=ms_num,student_num_id=student_num).location
    print(path.split("/")[-1])
    f = open(path, "rb")
    response = FileResponse(f, filename=path.split("/")[-1], as_attachment=True)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s'%quote(path.split("/")[-1])
    return response


def homework_management_page(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth

    page = "班级管理"
    path = get_image_path(student_num)

    student_count = models.student.objects.count()
    homework_list = [
        [x.deadline, x.title, x.subject, student_count - len(models.homework_upload.objects.filter(ms_num_id=x.ms_num)),
         x.ms_num] for x in
        models.message_homework.objects.all().order_by("-deadline")]
    return render(request, "management_homework.html", locals())


def homework_management_deal(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth
    ms_num = request.GET.get("message_id")
    order = request.GET.get("order")

    if order == "download":
        path = os.path.join(BASE_DIR,"static/Documents")
        dir_name = ms_num
        target_name = models.message_homework.objects.get(ms_num=ms_num).title
        command_1 = "cd " + path
        command_2 = "tar cvf " + target_name + ".tar " + dir_name
        command_3 = "gzip " + target_name + ".tar"
        print(command_1)
        print(command_2)
        print(command_3)
        os.system(command_1)
        os.system(command_2)
        os.system(command_3)
        filename = target_name + ".tar.gz"
        path = os.path.join(BASE_DIR,filename)
        f = open(path, "rb")
        response = FileResponse(f, filename=filename, as_attachment=True)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=%s' % quote(filename)
        return response


def homework_notuploadedlist_page(request):
    student_num = request.GET.get("student_num")
    auth = models.users.objects.get(student_num=student_num).auth
    ms_num = request.GET.get("message_id")
    title = models.message_homework.objects.get(ms_num=ms_num).title

    uploaded_student = [x.student_num_id for x in
                        models.homework_upload.objects.filter(ms_num_id=ms_num).order_by("-student_num_id")]
    not_uploaded_student_list = [x.student_num for x in models.student.objects.all() if
                                 x.student_num_id not in uploaded_student]
    not_uploaded_student = [[not_uploaded_student_list.index(x) + 1, models.student.objects.get(student_num=x)] for x in
                            not_uploaded_student_list]
    return render(request, "notuploaded_homework.html", locals())


def homework_notuploadedlist_deal(request):
    student_num = request.GET.get("student_num")
    target = request.GET.get("target")
    ms_num = request.GET.get("message_id")

    message = models.message_homework.objects.get(ms_num=ms_num)
    object = models.message_message.objects.create(title="作业提醒",description="记得在" + str(message.deadline) + "前提交" + message.title + "作业哦！！！！",
                                          send_person_student_num_id=str(student_num),target_student_num_id=str(target), useable=True)
    models.notice_message.objects.create(ms_num_id=object.ms_num, student_num_id=object.target_student_num_id)
    return homework_notuploadedlist_page(request)