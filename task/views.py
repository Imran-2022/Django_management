from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_Task(request):
    if request.method=='POST':
        post_form=forms.TaskForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('task') 
    else:
        post_form=forms.TaskForm()
    return render(request, 'task.html',{'form':post_form})

