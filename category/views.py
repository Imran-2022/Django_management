from django.shortcuts import render

# Create your views here.

def Category(request):
    return render(request,'category.html')