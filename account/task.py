from __future__ import absolute_import,unicode_literals
from celery import shared_task
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from dashboardapp.models import Dashboard,Quotes,Dommy

import  random

User = get_user_model()

@shared_task(bind=True)
def delete_unpaiduser(self):
    b=[]
    current_date = datetime.datetime.now()
    dashboard_object = Dashboard.objects.filter(payment_status="Un Paid")
    print('dashboard',dashboard_object)
    for i in dashboard_object:
        b.append(i.user)
    for i in b:    
        user_obj = User.objects.filter(id=i.id,create_date=current_date)
        if user_obj:
            for j in user_obj:
                j.delete()
                j.save()    

    return "Account deleted"

@shared_task(bind=True)
def quotesgenerate(self):

    lst=[]
    user_object = Quotes.objects.all()
    for i in user_object:
        lst.append(i.id)
    ranvalue = random.randint(min(lst),max(lst))
    c=ranvalue
    # randomobject = Quotes.objects.get(id=ranvalue)
    dommy = Dommy.objects.all()
    print(dommy)
    dommy.delete()
    for i in dommy:
        i.delete()
        i.save()
        print('deleted')
    Dommy.objects.create(number=ranvalue)
  

    return "Quotes generated Successfully"
