"""Define url patterns"""

from django.urls import path
from . import views

app_name='learning_logs'


urlpatterns=[
    
    #Home page
    path('', views.index, name='index'),

    #all topics
    path('topics/', views.topics, name='topics'),
    path('topic/<topic_id>/',views.topic,name='topic'),
    path('new_topic',views.new_topic,name='new_topic')
    ]

