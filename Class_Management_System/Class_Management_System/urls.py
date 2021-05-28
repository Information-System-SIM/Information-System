"""Class_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', views.login),
    path('login/', views.login),
    path('mainpage', views.mainpage),
    path('change_password/', views.change_password),
    path('index/homework/upload', views.homework_upload),
    # 把原先的message名字改成了messages_homework
    path('mainpage/messages_homework', views.message_homework),
    path('mainpage/messages_competition', views.message_competition),
    path('mainpage/messages_activity', views.message_activity),
    path('mainpage/messages_message', views.message_message),
    path('mainpage/message', views.message),
    path('management/notice_publishment/competition', views.competition_publishment),
    path('management/notice_publishment/activity', views.activity_publishment),
    path('management/notice_publishment/homework',views.homework_publishment),
    path('homework/homework_list',views.homework_list),
    path('homework/uploaded_homework',views.uploaded_homework),
    path('management/homework',views.homework_management),
    path('management/homework_notuploadedlist', views.homework_notuploadedlist),
    #获奖信息提交
    path('award/award_upload', views.upload_award)
]
