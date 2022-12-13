from random import choices
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from jobproject.utils import USERTYPE_CHOICES,EDUCATION_CHOICES,POSITION_CHOICES,SKILL_CHOICES


class Education(models.Model):
    qualification = models.CharField(max_length=250,choices=EDUCATION_CHOICES,default="bachelor")
    name = models.CharField(max_length=250)
    start_year = models.DateField()
    end_year = models.DateField()
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
         return self.name

class Project(models.Model):
    name = models.CharField(max_length=250)
    tools = models.TextField()
    feature = models.TextField()
    def __str__(self):
         return self.name

class Skills(models.Model):
    skills_type = models.CharField(max_length=250,choices=SKILL_CHOICES,default="technical")
    description = models.TextField()
    def __str__(self):
         return self.skills_type


class Experiences(models.Model):
    company_name = models.CharField(max_length=250)
    field_type = models.CharField(max_length=250)
    position = models.CharField(max_length=250,choices=POSITION_CHOICES,default="intern")
    objectives = models.TextField()
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.company_name





class Company(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    image = models.FileField(upload_to="profile",blank=True,null=True)
    location = models.CharField(max_length=250,null=True)
  
    def __str__(self):
        return self.name



class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 5 - 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator, MinLengthValidator(5)],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    image = models.FileField(upload_to="profile",blank=True,null=True)
    token  =models.CharField(max_length=150)
    location = models.CharField(max_length=250,null=True)
    number = models.CharField(max_length=250,null=True)
    salary = models.CharField(max_length=250,null=True)
    verify = models.BooleanField(default=False)
    user_type = models.CharField(max_length=250,choices=USERTYPE_CHOICES,default="Job_seeker")
    date = models.DateField(null=True)
    course = models.ManyToManyField(Course)
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experiences)
    project = models.ManyToManyField(Project)
    skill = models.ManyToManyField(Skills)
    hobby = models.CharField(max_length=250,null=True)
    whyneed = models.TextField(null=True)
    create_date = models.DateField(null=True)
    paymentend_date = models.DateField(null=True) 
    termscondition = models.BooleanField(default=False)

class TermsAndCondition(models.Model):
    description = models.TextField(null=True)

class Blog(models.Model):
    title = models.CharField(max_length=250,null=True)
    image = models.FileField(upload_to="media",null=True)
    description = models.TextField()
    date = models.DateField(null=True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=250,null=True)
    message = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=250,null=True)
