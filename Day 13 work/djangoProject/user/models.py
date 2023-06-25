from django.db import models

# Create your models here.

from django.db import models

# 不推荐使用python创建表结构

class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=4, default='男')

class ProvinceAndConfirmedTop10(models.Model):
    province = models.CharField(max_length=32, unique=True)
    confirmed = models.IntegerField()
