from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
