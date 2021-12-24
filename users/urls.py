"""为users定义rul模式"""
from typing import ParamSpec
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    #包含默认身份认证的URL，
    path('',include('django.contrib.auth.urls')),
]