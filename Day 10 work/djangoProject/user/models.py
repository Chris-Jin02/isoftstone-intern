from django.db import models

# Create your models here.

from django.db import models

# 不推荐使用python创建表结构

from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
