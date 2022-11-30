from random import choices
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from jobproject.utils import USERTYPE_CHOICES

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
    token  =models.CharField(max_length=150)
    verify = models.BooleanField(default=False)
    experience = models.TextField()
    user_type = models.CharField(max_length=250,choices=USERTYPE_CHOICES,default="Job_seeker")


class Company(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
  
    def __str__(self):
        return self.name
