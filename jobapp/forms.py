from jobapp.models import Category,Job
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['image','name', 'description']
        #For Label tag
        labels = {  
            'name': 'Name',
            'description': 'Description',
            'image':'Image',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["name"].widget.attrs={"class": 'form-control'}
            self.fields["description"].widget.attrs={"class": 'form-control'}   
            self.fields["image"].widget.attrs={"class": 'form-control'}   


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name','image', 'description','category']
        #For Label tag
        labels = {  
            'category': 'Category',
            'name': 'Name',
            'description': 'Description',
            'image':'Image',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["category"].widget.attrs={"class": 'form-control'}
            self.fields["name"].widget.attrs={"class": 'form-control'}
            self.fields["description"].widget.attrs={"class": 'form-control'}   
            self.fields["image"].widget.attrs={"class": 'form-control'}   
