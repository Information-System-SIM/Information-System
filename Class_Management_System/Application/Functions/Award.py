import os

import django.http
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Application import models
from Application.Functions.function import get_image_path, transfer_date, map_num2name
from django.contrib import messages
from Class_Management_System.settings import BASE_DIR, STATICFILES_DIRS


def message_notice(request):
    messages.success(request, "奖项上传成功")


def message_fail(request):
    messages.error(request, "请填写奖项名称")


def message_audit(request):
    messages.success(request, "奖项审核状态更新成功")


def map_code2level(level_str, order_str):
    dic_level = {"A":"国家级",
           "B":"省级",
           "C":"市级",
           "D":"校级",
           "E":"院级",
           }
    dic_order = {"A":"一等奖",
           "B":"二等奖",
           "C":"三等奖",
           "D":"优秀奖",
           "E":"参与",
           }
    level_str = dic_level[level_str]
    order_str = dic_order[order_str]
    return level_str + " " + order_str


def award_upload_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "提交获奖信息"

    return render(request, "award_upload.html", locals())


def award_list_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    # 输出奖项列表
    award_list = [[awd.uploaded_time,
                   awd.award_name,
                   map_num2name(awd.uploaded_stu_id),
                   map_code2level(awd.award_level, awd.award_order),
                   awd.apply_num]
                  for awd in models.award_apply.objects.filter(checked=None).order_by("uploaded_time")]
    return render(request, 'award_list.html', locals())


def award_upload_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]

    award_name = request.POST["award_name"]
    award_type = request.POST["award_type"]
    award_level = request.POST["award_level"]
    award_order = request.POST["award_order"]
    award_date = transfer_date(request.POST["award_date"])
    additional_text = request.POST["additional_text"]

    if award_name is not None and award_name != "":
        award_apply = models.award_apply.objects.create(award_name=award_name,
                                                        award_type=award_type,
                                                        award_level=award_level,
                                                        award_order=award_order,
                                                        award_date=award_date,
                                                        additional_text=additional_text,
                                                        uploaded_stu_id=student_num)
        message_notice(request)

        if request.FILES:
            file = request.FILES.get("demonstration")
            file_format = file.name.split(".")[-1]
            file_name = str(award_apply.apply_num) + "." + file_format
            path = os.path.join(STATICFILES_DIRS[0], "Award")
            with open(os.path.join(path, file_name), "wb+") as f:
                for chunk in file:
                    f.write(chunk)
        return award_upload_page(request)
    else:
        message_fail(request)
        return award_upload_page(request)


def award_audit_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    if auth != "Student":
        apply_num = request.GET.get("apply_num")
    else:
        HttpResponseRedirect("/login/")

    apply = models.award_apply.objects.get(apply_num=apply_num)
    student_name = map_num2name(apply.uploaded_stu_id)
    level, order = map_code2level(apply.award_level, apply.award_order).split(" ")
    filename = apply.filename
    if filename is not None:
        file_path = os.path.join(os.path.join(STATICFILES_DIRS, "Apply"), filename)
    return render(request, 'award_audit.html', locals())


def award_audit_deal(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    auth = request.session["auth"]

    if auth != "Student":
        apply_num = request.GET.get("apply_num")
        order = request.GET.get("order")
    else:
        HttpResponseRedirect("/login/")

    apply = models.award_apply.objects.get(apply_num=apply_num)
    if order == "0":
        apply.checked = "已通过"
        apply.save()
    else:
        apply.checked = "未通过"
        apply.save()
    message_audit(request)
    return HttpResponseRedirect("/management/award_list?student_num=" + student_num)


def award_audited_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "提交获奖信息"

    award_apply_lst = models.award_apply.objects.filter(uploaded_stu_id=student_num).order_by("-uploaded_time")
    award_lst = []
    for award in award_apply_lst:
        time = award.uploaded_time
        title = award.award_name
        value = map_code2level(award.award_level, award.award_order)
        if award.checked is None:
            checked = "未审核"
        else:
            checked = award.checked
        num = award.apply_num
        print(num)
        row = [time, title, value, checked, num]
        award_lst.append(row)
    return render(request, 'auditedaward_list.html', locals())


def award_content_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    apply_num = request.GET.get("apply_num")
    apply = models.award_apply.objects.get(apply_num=apply_num)
    student_name = map_num2name(apply.uploaded_stu_id)
    level, order = map_code2level(apply.award_level, apply.award_order).split(" ")
    filename = apply.filename
    if filename is not None:
        file_path = os.path.join(os.path.join(STATICFILES_DIRS, "Apply"), filename)
    return render(request, 'award_content.html', locals())
