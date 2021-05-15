from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=13)
    pwd = models.CharField(max_length=256)
    auth = models.CharField(max_length=256)