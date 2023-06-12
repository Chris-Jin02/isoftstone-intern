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


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', views.hello), # http://127.0.0.1:80/ 方式 1 --不要用，留给项目最后使用
    # url(r'hello/', views.hello), # http://127.0.0.1:8000/hello/ 方式 2
    # path('hello/', views.hello), # http://127.0.0.1:8000/hello/ 推荐使用 方式3
    # path('/', views.index), # / 保留字符
    url(r'^$', views.index),
    path('test/', views.test),
    path('ajax/', views.ajax),
    path('ajax_users/', views.ajax_users),
]
