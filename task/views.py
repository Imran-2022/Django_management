from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_Task(request):
    if request.method=='POST':
        post_form=forms.TaskForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage') 
    else:
        post_form=forms.TaskForm()
    return render(request, 'task.html',{'form':post_form})


def edit_task(request,id):
    
    post = models.Task.objects.get(pk=id)

    post_form=forms.TaskForm(instance=post) 

    if request.method=='POST': 
        post_form=forms.TaskForm(request.POST,instance=post) 
        if post_form.is_valid(): 
            post_form.save()
            return redirect('homepage') 
    return render(request, 'task.html',{'form':post_form})
