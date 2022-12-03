from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Company,Course,Education,Experiences,Project,Skills
from django.utils.safestring import mark_safe

User = get_user_model()

#Signupform
class AdminSignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", 
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password(Again)",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',

        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["username"].widget.attrs={"class": 'form-control'}
            self.fields["first_name"].widget.attrs={"class": 'form-control'}
            self.fields["last_name"].widget.attrs={"class": 'form-control'}   
            self.fields["email"].widget.attrs={"class": 'form-control'}   

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", 
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password(Again)",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
 
    course = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    education = forms.ModelMultipleChoiceField(
        queryset=Education.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    experience = forms.ModelMultipleChoiceField(
        queryset=Experiences.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    project= forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    skill= forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','course', 'education','experience','project','skill','password1', 'password2']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',

        }

    def save(self, commit=True):
        user = super().save()
        user.course.set(self.cleaned_data["course"])
        user.education.set(self.cleaned_data["education"])
        user.experience.set(self.cleaned_data["experience"])
        user.project.set(self.cleaned_data["project"])
        user.skill.set(self.cleaned_data["skill"])
        user.save()
        return user

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     valpwd = self.cleaned_data['password1']
    #     valrpwd = self.cleaned_data['password2']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError("Password doesnot match")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs={"class": 'form-control'}
        self.fields["first_name"].widget.attrs={"class": 'form-control'}
        self.fields["last_name"].widget.attrs={"class": 'form-control'}   
        self.fields["email"].widget.attrs={"class": 'form-control'}             

#login


class UserAuthentiationForm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs={"class": 'form-control'}
        self.fields["password"].widget.attrs= {"class": "form-control"}

#Company 
class CompanySignupForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", 
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password(Again)",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        fields = ['name', 'email', 'phone_number', 'password1', 'password2']
        #For Label tag
        labels = {  
            'name': 'Name',
            'phone_number': 'Phone Number',
            'email': 'Email',
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     valpwd = self.cleaned_data['password1']
    #     valrpwd = self.cleaned_data['password2']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError("Password doesnot match")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs={"class": 'form-control'}
        self.fields["phone_number"].widget.attrs={"class": 'form-control'}   
        self.fields["email"].widget.attrs={"class": 'form-control'}         