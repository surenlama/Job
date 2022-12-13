from jobapp.models import Category,Job,CVUpload
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['image','name', 'description','post_by']
        #For Label tag
        labels = {  
            'name': 'Name',
            'description': 'Description',
            'image':'Image',
            'post_by':'Post By'
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["name"].widget.attrs={"class": 'form-control'}
            self.fields["description"].widget.attrs={"class": 'form-control'}   
            self.fields["image"].widget.attrs={"class": 'form-control'}   
            self.fields["post_by"].widget.attrs={"class": 'form-control'}   



class JobForm(forms.ModelForm):
    # posted_date = forms.DateField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    class Meta:
        model = Job
        fields = ['category','name','image', 'description','location','salary_range','job_type','no_of_vacancy','knowledge','skill','abilities','education','expereince','post_by','posted_date']
        #For Label tag
        labels = {  
            'category': 'Category',
            'name': 'Name',
            'description': 'Description',
            'image':'Image',
            'post_by':'Post By',
            'location':'Location',
            'salary_range':'Salary Range',
            'job_type':'Job Type',
            'no_of_vacancy':'No Of Vacancy',
            'knowledge':'Knowledge Required',
            'skill':'Skillrequired',
            'abilities':'Abilities',
            'education':'Education',
            'expereince':'Experience',
            'posted_date':'Posted Date',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["category"].widget.attrs={"class": 'form-control'}
            self.fields["name"].widget.attrs={"class": 'form-control'}
            self.fields["description"].widget.attrs={"class": 'form-control'}   
            self.fields["image"].widget.attrs={"class": 'form-control'}   
            self.fields["post_by"].widget.attrs={"class": 'form-control'}  
            self.fields["location"].widget.attrs={"class": 'form-control'}   
            self.fields["salary_range"].widget.attrs={"class": 'form-control'}   
            self.fields["job_type"].widget.attrs={"class": 'form-control'}    
            self.fields["posted_date"].widget = forms.DateInput(attrs={"type": "date"})


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if kwargs.get("instance") is not None:
    #         self.initial["time"] = self.instance.date.time
    #         self.initial["dates"] = self.instance.date.date

    #     self.fields["location"].widget = forms.widgets.Select(choices=updated_location)

    #     self.fields["dates"].widget = forms.DateInput(attrs={"type": "date"})
class JobApplyform(forms.ModelForm):
    class Meta:
        model = CVUpload
        fields = ['name', 'job','cv']
        #For Label tag
        labels = {  
            'Name':'name',
            'CV':'cv',
            'Job':'job',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["job"].widget.attrs={"class": 'form-control'}       
        self.fields["cv"].widget.attrs={"class": 'form-control'}   
        self.fields["name"].widget.attrs={"class": 'form-control'}   

 
