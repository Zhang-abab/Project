from django import forms
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from learning_logs.models import Entry, Topic
from learning_logs.forms import TopicForm, EntryForm

def index(request):

    return render(request,'index.html')
@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    #topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其条目"""
    topic = Topic.objects.get(id = topic_id)
    #确认用户
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries }
    return render(request, 'topic.html', context)
@login_required
def new_topic(request):
    if request.method != 'POST':
        #未提交数据创建一个新表单
        form = TopicForm()
    else:
        #POST提交数据对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    #显示空表单无效
    context = {'form':form}
    return render(request, 'new_topic.html', context)
@login_required
def new_entry(request,topic_id):
    """在特定主题下添加条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'topic':topic, 'form':form}
    return render(request, 'new_entry.html', context)
@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.ownner != request.user:
        raise Http404
    if request.method != 'POST':
        #用当前条目填充表格
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据:对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'edit_entry.html', context)
    #pass;
# Create your views here.
