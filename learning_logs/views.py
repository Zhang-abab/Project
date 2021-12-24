from django.shortcuts import render

from learning_logs.models import Topic

def index(request):

    return render(request,'index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'topics.html', context)
# Create your views here.
