from .models import Dashboard
from django import forms
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()

class AdminDashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['qrcode','payment_type']
        #For Label tag
        labels = {  
            'payment_type': 'Payment Type',
            'qrcode': 'Qr code',        
        }
      
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["payment_type"].widget.attrs={"class": 'form-control'}
            self.fields["qrcode"].widget.attrs={"class": 'form-control'}

class JobDashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['user','bank_details','payment_screenshot','send_to']
        #For Label tag
        labels = {  
            'user':'User',
            'bank_details': 'Bank Details',
            'payment_screenshot': 'Payment Screenshot',
            'Send To':'send_to'
        }


      
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["user"].widget.attrs={"class": 'form-control'}   
            self.fields["bank_details"].widget.attrs={"class": 'form-control'}   
            # self.fields["send_to"].queryset=User.objects.filter(user_type="Job_seeker")

class JobDashboard1Form(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['user','bank_details','payment_screenshot','payment_status','apply_attempt']
        #For Label tag
        labels = {  
            'user':'User',
            'bank_details': 'Bank Details',
            'payment_screenshot': 'Payment Screenshot',
            'payment_status':'Status',  
            'apply_attempt':"Apply Attempt",
        }
      
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["user"].widget.attrs={"class": 'form-control'}   
            self.fields["bank_details"].widget.attrs={"class": 'form-control'}   
            self.fields["payment_screenshot"].widget.attrs={"class": 'form-control'}
            self.fields["payment_status"].widget.attrs={"class": 'form-control'}   
            self.fields["apply_attempt"].widget.attrs={"class": 'form-control'}   


# class QuotesForm(forms.ModelForm):
#     class Meta:
#         model = Quotes
#         fields = ['name','description']
#         #For Label tag
#         labels = {  
#             'name': 'Name',
#             'description': 'Description',        
#         }
      
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields["name"].widget.attrs={"class": 'form-control'}
#             self.fields["description"].widget.attrs={"class": 'form-control'}
