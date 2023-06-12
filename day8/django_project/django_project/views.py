# 小组：01
# 作者：姜何飞飞
# 创建时间：2023/6/9 9:53
# 文件名：views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def hello(request):
    return HttpResponse("hello world!")


def index(request):
    print('index...')
    return render(request, "index.html")


def test(request):
    print('test...')
    return render(request, "hello.html")


def ajax(request):
    return HttpResponse("hello world!")


def ajax_users(request):
    userList = [
        {'userid': 1, 'username': '张三', 'password': 'asdf'},
        {'userid': 2, 'username': '李四', 'password': 'ghjkl'},
        {'userid': 3, 'username': '王五', 'password': 'qwert'},
    ]
    return JsonResponse(userList, safe=False)
