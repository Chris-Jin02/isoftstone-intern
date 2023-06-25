#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/9 10:48
"""
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world!")


def index(request):
    print('index...')
    return render(request, "index.html")


def test(request):
    print('test...')
    # content = {}
    # content['name'] = '风清扬'
    var1='任盈盈'
    return render(request, "test.html",{'name':var1})


def ajax(request):

    return HttpResponse("hello world!")

def ajax_users(request):
    userList=[
              {'userid':1,'username':'张三','password':'asdf'},
              {'userid':2,'username':'李四','password':'ghjkl'},
              {'userid':3,'username': '王五', 'password': 'qwert'},
              ]
    return HttpResponse(userList)


def listDemo(request):
    # list1 = ['django0', 'django1', 'django2', 'django3']
    list1 = []
    # list1=None
    return render(request, 'test.html', {'list1': list1})


def dateDemo(request):
    import datetime
    now = datetime.datetime.now()
    return render(request, 'test.html', {'now': now})


def filesizeformatDemo(request):
    fileSize1 = 1024 * 2  # 2K
    fileSize2 = 1024 * 1024 * 2  # 2M
    fileSize3 = 1024 * 1024 * 1024 * 2  # 2G
    fileSize4 = 1024 * 1024 * 1024 * 1024 * 2  # 2T
    fileSizeList = [fileSize1, fileSize2, fileSize3, fileSize4]
    return render(request, 'test.html', {'fileSizeList': fileSizeList})


def ifElseDemo(request):
    import random
    num = random.randint(1, 100)  # 1-100的随机数
    return render(request, 'test.html', {'num': num})


def dictDemo2(request):
    userInfo = {'username': 'zhangsan', 'age': '25', 'sex': '男'}
    return render(request, 'test.html', {'userInfo': userInfo})
