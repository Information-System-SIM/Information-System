from django.shortcuts import render
from Application import models
from Application.Functions import Login, Document_Management
from Application.Functions.Homework import homework_page, uploaded_homework_deal, homework_management_page, \
    homework_management_deal, homework_notuploadedlist_page, homework_notuploadedlist_deal
from Application.Functions.MainPage import mainpage_show
from Application.Functions.Message import message_homework_page, message_competition_page, message_activity_page, \
    message_message_page, detailed_message_page, competition_publishment_page, activity_publishment_page, \
    homework_publishment_page
from Application.Functions.Message_Publishment import competition_publishment_deal, activity_publishment_deal, \
    homework_publishment_deal

# Create your views here.
from Application.Functions.function import get_image_path


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


def table(request):
    datas = models.users.objects.all()
    print("datas:")
    print(datas)
    return render(request, 'tables-basic.html', {"datas": datas})


def change_password(request):
    if request.method == "GET":
        return render(request, "pages-changeid.html")
    elif request.method == "POST":
        return Login.change_password(request)


def homework_upload(request):
    if request.method == "get":
        student_num = request.GET.get("student_num")
        homework_name = request.GET.get("homework_name")
        return render(request, "document_upload.html", {"student_num": student_num, "homework_name": homework_name})
    elif request.method == "POST":
        student_num = request.POST["student_num"]
        homework_name = request.POST["homework_name"]
        Document_Management.homework_upload(request, student_num, homework_name)
        return render(request, "document_upload.html")
    else:
        student_num = request.GET.get("student_num")
        homework_name = request.GET.get("homework_name")
        return render(request, "document_upload.html", {"student_num": student_num, "homework_name": homework_name})


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
        student_num = request.GET.get("student_num")
        message_id = request.GET.get("message_id")
        upload_resault = Document_Management.homework_upload(request, student_num, message_id)
        print(upload_resault)
        return detailed_message_page(request,upload_resault)


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
        student_num = request.GET.get("student_num")
        auth = models.users.objects.get(student_num=student_num).auth

        homework_list = [[x.deadline, x.title, x.subject, x.text, x.ms_num] for x in models.message_homework.objects.filter(useable=True).order_by("-deadline")]
        homework_msnum = [x.ms_num for x in models.message_homework.objects.filter(useable=True)]
        for ms_num in homework_msnum:
            try:
                upload = models.homework_upload.objects.get(ms_num_id=ms_num,student_num_id=student_num)
                index = homework_msnum.index(ms_num)
                homework_list[index].append(True)
            except:
                index = homework_msnum.index(ms_num)
                homework_list[index].append(False)
        return render(request, "homework_list.html", locals())


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