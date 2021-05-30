from django.shortcuts import render
from Application.Functions import Login, Document_Management
from Application.Functions.Activity_Score import activity_score_page, class_activity_score_page
from Application.Functions.Award import award_upload_page, award_upload_deal, award_list_page, award_audit_page, \
    award_audit_deal, award_audited_page, award_content_page
from Application.Functions.Gallery import gallery_page
from Application.Functions.Homework import homework_page, uploaded_homework_deal, homework_management_page, \
    homework_management_deal, homework_notuploadedlist_page, homework_notuploadedlist_deal, homework_list_page
from Application.Functions.MainPage import mainpage_show
from Application.Functions.Message import message_homework_page, message_competition_page, message_activity_page, \
    message_message_page, detailed_message_page, competition_publishment_page, activity_publishment_page, \
    homework_publishment_page, unnoticed_message_management_page, detailed_message_deal, unnoticed_message_stulist_page, \
    unnoticed_message_stulist_deal
from Application.Functions.Message_Publishment import competition_publishment_deal, activity_publishment_deal, \
    homework_publishment_deal

# Create your views here.
from Application.Functions.function import get_image_path, transfer_date


def mainpage(request):
    if request.method == "GET":
        return mainpage_show(request)
    else:
        pass


def login(request):
    if request.method == "GET":
        return render(request, "pages-signin.html")
    elif request.method == "POST":
        return Login.login(request)


def change_password(request):
    if request.method == "GET":
        return render(request, "pages-changeid.html")
    elif request.method == "POST":
        return Login.change_password(request)


# 作业通知
def message_homework(request):
    if request.method == "GET":
        return message_homework_page(request)


# 比赛通知
def message_competition(request):
    if request.method == "GET":
        return message_competition_page(request)


# 活动通知
def message_activity(request):
    if request.method == "GET":
        return message_activity_page(request)


# 通知消息
def message_message(request):
    if request.method == "GET":
        return message_message_page(request)


# 查看消息详情
def message(request):
    if request.method != "POST":
        return detailed_message_page(request)
    else:
        return detailed_message_deal(request)


def competition_publishment(request):
    if request.method == "GET":
        return competition_publishment_page(request)
    elif request.method == "POST":
        return competition_publishment_deal(request)


def activity_publishment(request):
    if request.method == "GET":
        return activity_publishment_page(request)
    elif request.method == "POST":
        return activity_publishment_deal(request)


def homework_publishment(request):
    if request.method == "GET":
        return homework_publishment_page(request)
    elif request.method == "POST":
        return homework_publishment_deal(request)


def homework_list(request):
    if request.method != "POST":
        return homework_list_page(request)


def uploaded_homework(request):
    if request.method != "POST":
        return homework_page(request)
    else:
        return uploaded_homework_deal(request)


def homework_management(request):
    if request.method != "POST":
        return homework_management_page(request)
    else:
        return homework_management_deal(request)


def homework_notuploadedlist(request):
    if request.method != "POST":
        return homework_notuploadedlist_page(request)
    elif request.method == "POST":
        return homework_notuploadedlist_deal(request)


def upload_award(request):
    if request.method != "POST":
        return award_upload_page(request)
    else:
        return award_upload_deal(request)


def award_list(request):
    if request.method != "POST":
        return award_list_page(request)
    else:
        return award_list_page(request)


def award_audit(request):
    if request.method != "POST":
        return award_audit_page(request)
    else:
        return award_audit_deal(request)


def award_audited(request):
    if request.method != "POST":
        return award_audited_page(request)


def award_content(request):
    if request.method != "POST":
        return award_content_page(request)


def activity_score(request):
    if request.method !="POST":
        return activity_score_page(request)


def gallery(request):
    if request.method != "POST":
        return gallery_page(request)


def class_activity_score(request):
    if request.method != "POST":
        return class_activity_score_page(request)


def unnoticed_message_management(request):
    if request.method != "POST":
        return unnoticed_message_management_page(request)


def unnoticed_message_stulist(request):
    if request.method != "POST":
        return unnoticed_message_stulist_page(request)
    else:
        return unnoticed_message_stulist_deal(request)
