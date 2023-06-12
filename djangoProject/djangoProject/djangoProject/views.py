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
    return render(request, "test.html")


def ajax(request):
    return HttpResponse("hello world!")

def ajax_users(request):
    print('1')
    userList=[
              {'userid':1,'username':'张三','password':'asdf'},
              {'userid':2,'username':'李四','password':'ghjkl'},
              {'userid':3,'username': '王五', 'password': 'qwert'},
              ]
    return HttpResponse(userList)
