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

class message_homework(models.Model):
    ms_num = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=256)
    text = models.TextField()
    Requirement = models.TextField()
    subject = models.CharField(max_length=256)
    published_time = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    useable = models.BooleanField(auto_created=True)

class notice_homework(models.Model):
    id = models.AutoField(primary_key=True)
    ms_num = models.ForeignKey(message_homework, on_delete=models.DO_NOTHING)
    student_num = models.ForeignKey(student, on_delete=models.DO_NOTHING)