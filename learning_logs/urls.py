"""定义learning_logs的URL模式"""
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'learning_logs'

#主页
urlpatterns = [
    #主页
    path('',views.index, name='index'),
]