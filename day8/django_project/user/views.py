from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Users
import json

def testAdd(request):
    print('添加...')
    user = Users(username='令狐冲 4', password='dgjj')
    user.save()
    return HttpResponse("添加成功!")

def removeUserByUserid(request):
    print('删除...')
    user = Users(userid=2)
    user.delete()
    return HttpResponse("删除成功!")

def modifyUserByUserid(request):
    print('修改...')
    user = Users(userid=2)
    user.username = '任我行'
    user.save()  # 如果id存在就为修改，否则为添加
    return HttpResponse("修改成功!")

def getUserInfoByUserid(request):
    # 通过地址栏拼参访问此方法（get请求），获取get请求url中的id所对应的值
    userid = request.GET.get('userid')
    print('查询一个')
    user = Users.objects.get(userid=userid)
    #user = Users.objects.get(userid=2)
    print(user.userid)
    print(user.username)
    print(user.password)
    # print(user.sex)
    return HttpResponse(user.username)

def getAllUserInfo(request):
    print('查询所有')
    userList = Users.objects.all()
    from utils import querySetToJson
    res = querySetToJson(userList.values())
    return HttpResponse(res)

def signin(request):
    print('登录')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = Users.objects.get(username=username, password=password)
        user = json.dumps(user, default=lambda o: o.__dict__, ensure_ascii=False)
        return redirect('/test')
    return render(request, 'login.html')

