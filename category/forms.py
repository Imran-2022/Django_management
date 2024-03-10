from   django import forms
from . models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'
        # sb field nea ekta form create kre dbe...
        # exclude= []
        # fields=['name','abc]

        