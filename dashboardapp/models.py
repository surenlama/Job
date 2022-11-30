from django.db import models
from django.utils.translation import gettext_lazy as _
from jobproject.utils import PAYMENT_CHOICES,PAY_CHOICES


class Dashboard(models.Model):
    payment_type = models.CharField(max_length=250,choices=PAYMENT_CHOICES,default="paypal")
    qrcode=models.FileField(upload_to="media",null=True)
    name=models.CharField(max_length=250,null=True)
    bank_details = models.TextField()
    payment_screenshot = models.FileField(upload_to="media",null=True)
    added_on=models.DateTimeField(null=True)
    payment_status = models.CharField(max_length=250,choices=PAY_CHOICES,default="unpaid")


