from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

@login_required
def check_topic_owner(request, topic):
    if topic is None:
        return False
    return topic.owner == request.user

def index(request):
    """学习的主题的主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """topic 详细信息"""
    topic = Topic.objects.filter(id=topic_id).first()
    if not check_topic_owner(request, topic):
        return render(request, 'learning_logs/404.html')
    entries = topic.entry_set.order_by('-date_added')
    print(entries)
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据,创建一个新的表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """给指定的主题添加条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)

    topic = entry.topic
    if not check_topic_owner(request, topic):
        return render(request, 'learning_logs/404.html')

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    pass
