from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.

def index(request):
    """学习的主题的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """topics"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """topic 详细信息"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    print(entries)
    context = {'topic': topic, 'entries': entries}
    return  render(request, 'learning_logs/topic.html', context)