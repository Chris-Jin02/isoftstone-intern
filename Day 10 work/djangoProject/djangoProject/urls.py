from django.contrib import admin
from django.urls import path
# from django.urls import re_path as url  #4.0以上使用这个
from django.conf.urls import url
from django.urls import path
from . import views
import user.views

from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from . import views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index),
    path('test/', views.test),
    path('ajax/', views.ajax),
    path('ajax_users/', views.ajax_users),



# ORM
    path('user/testAdd/', user.views.testAdd),
    path('user/removeUserByUserid/', user.views.removeUserByUserid),
    path('user/modifyUserByUserid/', user.views.modifyUserByUserid),
    path('user/getUserInfoByUserid/', user.views.getUserInfoByUserid),
    path('user/getAllUserInfo/', user.views.getAllUserInfo),
    path('user/login/', user.views.signin, name='/login'),

]
