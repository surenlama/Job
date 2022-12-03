from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)
    added_on=models.DateTimeField(null=True)
    post_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)
    post_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class CVUpload(models.Model):
    name = models.CharField(max_length=250,null=True)
    cv = models.FileField(upload_to="media",null=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="cvjob",null=True)

