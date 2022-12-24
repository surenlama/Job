from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from  jobproject.utils import CV_CHOICES,JOB_CHOICES,CATEGORY_CHOICES
User = get_user_model()


class MainCategory(models.Model):
    category_type = models.CharField(max_length=250,choices=CATEGORY_CHOICES,default="digital")
    description = models.TextField(null=True)
    def __str__(self):
        return self.category_type


class Category(models.Model):
    main = models.ForeignKey(MainCategory,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)
    added_on=models.DateTimeField(null=True)
    post_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category_type = models.CharField(max_length=250,choices=CATEGORY_CHOICES,default="digital")

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=250,null=True)
    image = models.FileField(upload_to="media",null=True)
    def __str__(self):
        return self.name


class Job(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="catjob")
    name=models.CharField(max_length=250,null=True)
    image=models.FileField(upload_to="media",null=True)
    description=models.TextField(max_length=250,null=True)
    post_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(null=True)
    salary_range = models.CharField(max_length=250,null=True)
    job_type = models.CharField(max_length=250,choices=JOB_CHOICES,default="fulltime")
    no_of_vacancy = models.CharField(max_length=250,null=True)
    knowledge = models.TextField(null=True)
    skill = models.TextField(null=True)
    abilities = models.TextField(null=True)
    education = models.TextField(null=True)
    expereince = models.TextField(null=True)
    application_date = models.DateField(null=True)
    posted_date = models.DateField(null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

class CVUpload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=250,null=True)
    cv = models.FileField(upload_to="media",null=True)
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="cvjob",null=True)
    # status = models.CharField(max_length=250,choices=CV_CHOICES,default="notview")

# class FreelancingSubCategory(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     name=models.CharField(max_length=250,null=True)
#     image=models.FileField(upload_to="media",null=True)
#     description=models.TextField(max_length=250,null=True)