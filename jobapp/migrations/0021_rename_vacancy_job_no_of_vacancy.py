# Generated by Django 4.0.6 on 2022-12-10 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0020_job_vacancy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='vacancy',
            new_name='no_of_vacancy',
        ),
    ]
