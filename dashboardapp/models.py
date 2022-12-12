from django.db import models
from django.utils.translation import gettext_lazy as _
from jobproject.utils import PAYMENT_CHOICES,PAY_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()



class Dashboard(models.Model):
    payment_type = models.CharField(max_length=250,choices=PAYMENT_CHOICES,default="paypal")
    qrcode=models.FileField(upload_to="media",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="dashuser",null=True)
    bank_details = models.TextField()
    payment_screenshot = models.FileField(upload_to="media",null=True)
    added_on=models.DateTimeField(null=True)
    payment_status = models.CharField(max_length=250,choices=PAY_CHOICES,default="Un Paid")
    send_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    apply_attempt = models.IntegerField(default=0)

    # @property
    # def applychance(self):
    #     return ""+str(self.apply_attempt)
class Quotes(models.Model):
    name = models.CharField(max_length=250,null=True)
    description = models.TextField()

class Dommy(models.Model):
    number = models.IntegerField() 
