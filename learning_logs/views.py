from django import forms
from django.shortcuts import render, redirect

from learning_logs.models import Topic
from learning_logs.forms import TopicForm

def index(request):

    return render(request,'index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其条目"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries }
    return render(request, 'topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        #未提交数据创建一个新表单
        form = TopicForm()
    else:
        #POST提交数据对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    #显示空表单无效
    context = {'form':form}
    return render(request, 'new_topic.html', context)
# Create your views here.
