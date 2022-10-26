"""定义learning_logs的URL模式"""
from django.urls import  path
from . import  views

app_name = 'learning_logs'

urlpatterns = [
    # home 没有指定path
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
]

