from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)
    added_on=models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)

    def __str__(self):
        return self.name