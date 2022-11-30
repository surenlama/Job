from .models import Dashboard
from django import forms
from django.contrib.auth import get_user_model

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
        fields = ['name','bank_details','payment_screenshot']
        #For Label tag
        labels = {  
            'name':'Name',
            'bank_details': 'Bank Details',
            'payment_screenshot': 'Payment Screenshot',
            # 'payment_status':'Status',  
        }
      
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["name"].widget.attrs={"class": 'form-control'}   
            self.fields["bank_details"].widget.attrs={"class": 'form-control'}   
            self.fields["payment_screenshot"].widget.attrs={"class": 'form-control'}
            # self.fields["payment_status"].widget.attrs={"class": 'form-control'}   
