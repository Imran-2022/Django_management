from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def Category(request):
    if request.method=='POST': # user post request koreche
        category_form=forms.CategoryForm(request.POST) # user er post request data ekhane capture krlm.
        if category_form.is_valid(): #post kra dt valid kina check .!
            category_form.save() # jdi valid hy. database a save krbo
            return redirect('category') 
    else: # user normally website a gle blank form pbe !!! 
        category_form=forms.CategoryForm()
    return render(request, 'category.html',{'form':category_form})