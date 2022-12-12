from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobproject.settings')


app=Celery('jobproject')
app.conf.update(timezone = 'Asia/kathmandu')
app.config_from_cmdline
app.config_from_object(settings,namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))