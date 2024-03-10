
from django.shortcuts import render,redirect
from task.models import Task

def home(request):
    data = Task.objects.all()
    # print(data)
    # for i in data:
        # print(i.title,i.category)
        # for j in i.category.all():
        #     print(j)
    
    return render(request,'home.html', {'data':data})


def delete_task(request,id):
    post = Task.objects.get(pk=id)
    post.delete()
    return redirect('homepage') 