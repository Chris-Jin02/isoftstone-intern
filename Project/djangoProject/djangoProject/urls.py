"""skd_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.urls import re_path as url  #4.0以上使用这个
from django.conf.urls import url
from . import views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index),
    #项目

    #关键词雷达图
    path('user/getkeywords/', user.views.getkeywords),
    #各个月发表量
    #动态柱状图
    path('user/get_total/', user.views.get_total),
    #预测数据
    path('user/Forecastdata/', user.views.Forecastdata),
    #关系花图
    path('user/relationdata/', user.views.relationdata),
    #rose
    path('user/get_chart_data/', user.views.get_chart_data)
]