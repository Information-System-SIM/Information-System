from django.db import models


# Create your models here.

class users(models.Model):
    student_num = models.CharField(max_length=13, primary_key=True)
    pwd = models.CharField(max_length=256)
    auth = models.CharField(max_length=256)


class student(models.Model):
    student_num = models.ForeignKey('users', on_delete=models.CASCADE, primary_key=True)
    student_name = models.CharField(max_length=256)
    student_phone = models.CharField(max_length=11)
    student_email = models.CharField(max_length=256)
    self_description = models.TextField(null="请填写你的个人简介")
    image = models.ImageField(default=None, null=True, blank=True, upload_to='IMG/')


class message_homework(models.Model):
    ms_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    text = models.TextField()
    Requirement = models.TextField()
    subject = models.CharField(max_length=256)
    published_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    useable = models.BooleanField()

    def get_time(self):
        # date = str(self.published_time.date)
        print(self.published_time)
        print("1")

class notice_homework(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_homework, on_delete=models.DO_NOTHING)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)


# 比赛/活动/其他消息
# 属性：
#   消息编号
#   标题
#   文本
#   发布时间
#   是否可用

class message_competition(models.Model):
    ms_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    useable = models.BooleanField()
    competition_time = models.DateTimeField()
    published_time = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=256)


# 比赛/活动/其他通知
# 属性：
#   通知编号
#   对应消息的编号
#   学号

class notice_competition(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_competition, on_delete=models.DO_NOTHING)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)

class message_activity(models.Model):
    ms_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    useable = models.BooleanField()
    activity_time = models.DateTimeField()
    published_time = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=256)

class notice_activity(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_activity, on_delete=models.DO_NOTHING)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)

class message_message(models.Model):
    ms_num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    href = models.CharField(max_length=256)
    send_person_student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING, related_name="send")
    target_student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING, related_name="target")
    published_time = models.DateTimeField(auto_now=True)
    useable = models.BooleanField()

class notice_message(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_message, on_delete=models.DO_NOTHING)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)

class homework_upload(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_homework, on_delete=models.CASCADE)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=256)