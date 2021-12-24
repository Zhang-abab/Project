"""为users定义rul模式"""
from typing import ParamSpec
from django.urls import path, include
from . import views
app_name = 'users'

urlpatterns = [
    #包含默认身份认证的URL，
    path('',include('django.contrib.auth.urls')),
    #注册页面
    path('register/', views.register,name='register')
]