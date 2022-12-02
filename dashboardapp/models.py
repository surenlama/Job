from django.db import models
from django.utils.translation import gettext_lazy as _
from jobproject.utils import PAYMENT_CHOICES,PAY_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()



class Dashboard(models.Model):
    payment_type = models.CharField(max_length=250,choices=PAYMENT_CHOICES,default="paypal")
    qrcode=models.FileField(upload_to="media",null=True)
    name=models.CharField(max_length=250,null=True)
    bank_details = models.TextField()
    payment_screenshot = models.ImageField(upload_to="media",null=True)
    added_on=models.DateTimeField(null=True)
    payment_status = models.CharField(max_length=250,choices=PAY_CHOICES,default="unpaid")
    send_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

