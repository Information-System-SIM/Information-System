import os
from urllib.parse import quote

from django.http import FileResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Application import models
from Application.Functions.function import get_image_path
from Class_Management_System.settings import BASE_DIR
import tkinter.messagebox as ms


def homework_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "提交作业"

    uploaded_msnum = [x.ms_num_id for x in models.homework_upload.objects.filter(student_num_id=student_num)]
    homework_list = [[x.deadline, x.title, x.subject, x.text, x.ms_num] for x in
                     models.message_homework.objects.filter(useable=True).order_by("-deadline") if
                     x.ms_num in uploaded_msnum]

    return render(request, "uploaded_homework.html", locals())


def uploaded_homework_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]

    ms_num = request.GET.get("message_id")
    order = request.GET.get("order")

    if order == "download":
        return download(student_num, ms_num)
    elif order == "delete":
        delete(student_num, ms_num)
        return homework_page(request)


def delete(student_num, ms_num):
    filename = models.homework_upload.objects.get(ms_num_id=ms_num, student_num_id=student_num).location
    os.remove(os.path.join(BASE_DIR, 'static', 'Documents', str(ms_num), filename))
    models.homework_upload.objects.get(student_num_id=student_num, ms_num_id=ms_num).delete()


def download(student_num, ms_num):
    filename = models.homework_upload.objects.get(ms_num_id=ms_num, student_num_id=student_num).location
    path = os.path.join(BASE_DIR, 'static', 'Documents', str(ms_num), filename)
    f = open(path, "rb")
    response = FileResponse(f, filename=filename, as_attachment=True)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' % quote(path.split("/")[-1])
    return response


def homework_management_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    student_count = models.student.objects.count()
    homework_list = [
        [x.deadline, x.title, x.subject, student_count - len(models.homework_upload.objects.filter(ms_num_id=x.ms_num)),
         x.ms_num] for x in
        models.message_homework.objects.all().order_by("-deadline")]
    return render(request, "management_homework.html", locals())


def homework_management_deal(request):
    # 获取学生学号、姓名、auth
    auth = request.session["auth"]

    if auth == "Study":
        ms_num = request.GET.get("message_id")
        order = request.GET.get("order")
    else:
        return HttpResponseRedirect("/login/")

    if order == "download":
        path = os.path.join(BASE_DIR, "static/Documents")
        dir_name = ms_num
        target_name = models.message_homework.objects.get(ms_num=ms_num).title
        os.chdir(os.path.join(BASE_DIR, "static/Documents"))
        command_2 = "tar cvf " + target_name + ".tar" + " " + dir_name
        command_3 = "gzip " + target_name + ".tar"
        print(command_2)
        print(command_3)
        os.system(command_2)
        os.system(command_3)
        filename = target_name + ".tar.gz"
        path = os.path.join(path, filename)
        f = open(path, "rb")
        response = FileResponse(f, filename=filename, as_attachment=True)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=%s' % quote(filename)
        os.remove(path)
        return response


def homework_notuploadedlist_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    if auth == "Study":
        ms_num = request.GET.get("message_id")
        title = models.message_homework.objects.get(ms_num=ms_num).title
    else:
        return HttpResponseRedirect("/login/")

    uploaded_student = [x.student_num_id for x in
                        models.homework_upload.objects.filter(ms_num_id=ms_num).order_by("-student_num_id")]
    not_uploaded_student_list = [x.student_num for x in models.student.objects.all() if
                                 x.student_num_id not in uploaded_student]
    not_uploaded_student = [[not_uploaded_student_list.index(x) + 1, models.student.objects.get(student_num=x)] for x in
                            not_uploaded_student_list]
    return render(request, "notuploaded_homework.html", locals())


def homework_notuploadedlist_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    auth = request.session["auth"]

    if auth == "Study":
        target = request.GET.get("target")
        ms_num = request.GET.get("message_id")
    else:
        return HttpResponseRedirect("/login/")

    if target == "all":
        message = models.message_homework.objects.get(ms_num=ms_num)
        students = [message.student_num_id for message in models.homework_upload.objects.filter(ms_num_id=ms_num)]
        for student in students:
            print(student)
            object = models.message_message.objects.create(title="作业提醒", description="记得在" + str(
                message.deadline) + "前提交" + message.title + "作业哦！！！！",
                                                           send_person_student_num_id=str(student_num),
                                                           target_student_num_id=str(student), useable=True)
            models.notice_message.objects.create(ms_num_id=object.ms_num, student_num_id=object.target_student_num_id)
            return homework_notuploadedlist_page(request)

    message = models.message_homework.objects.get(ms_num=ms_num)
    object = models.message_message.objects.create(title="作业提醒", description="记得在" + str(
        message.deadline) + "前提交" + message.title + "作业哦！！！！",
                                                   send_person_student_num_id=str(student_num),
                                                   target_student_num_id=str(target), useable=True)
    models.notice_message.objects.create(ms_num_id=object.ms_num, student_num_id=object.target_student_num_id)
    return homework_notuploadedlist_page(request)


def homework_list_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "提交作业"

    homework_list = [[x.deadline, x.title, x.subject, x.text, x.ms_num] for x in
                     models.message_homework.objects.filter(useable=True).order_by("-deadline")]
    homework_msnum = [x.ms_num for x in models.message_homework.objects.filter(useable=True)]
    for ms_num in homework_msnum:
        try:
            upload = models.homework_upload.objects.get(ms_num_id=ms_num, student_num_id=student_num)
            index = homework_msnum.index(ms_num)
            homework_list[index].append(True)
        except:
            index = homework_msnum.index(ms_num)
            homework_list[index].append(False)
    return render(request, "homework_list.html", locals())
