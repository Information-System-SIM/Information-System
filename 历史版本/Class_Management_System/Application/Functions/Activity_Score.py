from django.shortcuts import render
from Application import models
from Application.Functions.Award import map_code2level
from Application.Functions.function import get_image_path, map_num2name


def map_code2score(level, order):
    dic_level = {"A":5,
                 "B":4,
                 "C":3,
                 "D":2,
                 "E":1}
    dic_order = {"A":5,
                 "B":4,
                 "C":3,
                 "D":2,
                 "E":1}
    return dic_level[level] * dic_order[order]


def lst_sum(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum


def activity_score_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "活动分查看"

    awards = models.award_apply.objects.filter(uploaded_stu_id=student_num, checked="已通过")
    award_lst = [[award.award_date,
                  award.award_name,
                  map_code2level(award.award_level, award.award_order),
                  award.award_type,
                  map_code2score(award.award_level, award.award_order),
                  award.apply_num]
                 for award in awards]
    total = lst_sum([x[4] for x in award_lst])
    return render(request, 'activity_score_list.html', locals())


def class_activity_score_page(request):
    # 获取学生学号、姓名、auth
    student_num = request.session["student_num"]
    student_name = request.session["student_name"]
    auth = request.session["auth"]
    message_num = request.session["message_num"]
    path = request.session["path"]

    # 用于优化页面细节
    page = "班级管理"

    awards = models.award_apply.objects.filter(checked="已通过")
    award_lst = [[award.award_date,
                  award.award_name,
                  map_code2level(award.award_level, award.award_order),
                  award.award_type,
                  map_num2name(award.uploaded_stu_id),
                  map_code2score(award.award_level, award.award_order),
                  award.apply_num]
                 for award in awards]
    total = lst_sum([x[5] for x in award_lst])
    return render(request, 'class_activity_score_list.html', locals())