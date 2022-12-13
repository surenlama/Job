from django.contrib import admin
from .models import Category,Job,CVUpload,Location
# Register your models here.
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(CVUpload)
admin.site.register(Location)