from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.
from user.models import Users

def testAdd(request):
    print('添加...')
    user = Users(userid=2 ,username='任我行2', password='电饭锅2')
    user.save() #保存
    return HttpResponse("添加成功!")

def removeUserByUserid(request):
    print('删除...')
    user = Users(userid=1)
    user.delete()
    return HttpResponse("删除成功!")

def modifyUserByUserid(request):
    print('修改...')
    user = Users(userid=2)
    user.username='任我行'
    user.save()  # 如果id存在就为修改，否则为添加
    return HttpResponse("修改成功!")

def getUserInfoByUserid(request):
    # 通过地址栏拼参访问此方法（get请求），获取get请求url中的id所对应的值
    id=request.GET.get('id')
    print('查询一个')
    user = Users.objects.get(userid=id)
    # user=Users.objects.get(userid=3)
    print(user.userid)
    print(user.username)
    print(user.password)
    print(user.sex)

    return HttpResponse(user.username)


def getAllUserInfo(request):
    print('查询所有')
    userList=Users.objects.all()
    from utils import querySetToJson
    res = querySetToJson(userList.values())
    return HttpResponse(res, content_type='application/json')