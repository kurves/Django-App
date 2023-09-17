from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PersonForm
u from django.contrib.auth import LogoutView


# Create your views here.

def index(request):

    return render(request, 'learning_logs/index.html')

def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.all()
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):


    if request == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    else:
        form =PersonForm()
    context={'form':form}
    return render(request, 'learning_logs/new_topic.html',context)



def Logout_viw