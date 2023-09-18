from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username)
            LoginView(request, authenticated_user)
            return HttpResposeredirect(reverse, "learning_logs:index")
    else:
        form=UserCreationForm()    
    context={'form':form}        
    return render(request,'users/register.html',context)