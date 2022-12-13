from django.contrib import admin
from account.models import User,Company,Experiences,Project,Skills,Education,Course,\
    TermsAndCondition,Blog,Contact
# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Experiences)
admin.site.register(Education)
admin.site.register(Course)
admin.site.register(TermsAndCondition)
admin.site.register(Blog)
admin.site.register(Contact)
