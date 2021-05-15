from django.db import models

# Create your models here.

class users(models.Model):
    student_num = models.CharField(max_length=13, primary_key=True)
    pwd = models.CharField(max_length=256)
    auth = models.CharField(max_length=256)