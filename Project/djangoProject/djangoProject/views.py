#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    作者:杜丹东
    日期:2023/6/9 10:48
"""
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    print('index...')
    return render(request, "index.html")
