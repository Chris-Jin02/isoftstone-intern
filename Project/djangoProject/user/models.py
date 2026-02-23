from django.db import models

# Create your models here.

from django.db import models

# 不推荐使用python创建表结构
class keywords(models.Model):
    frequency = models.CharField(max_length=32)

class total(models.Model):
    date = models.CharField(max_length=32)
    Paper_Num = models.IntegerField()
    subject = models.CharField(max_length=32)

class Forecast(models.Model):
    date = models.CharField(max_length=32)
    category = models.IntegerField()
    number = models.CharField(max_length=32)

class Papers(models.Model):
    word = models.CharField(max_length=128)
    frequency = models.CharField(max_length=32)