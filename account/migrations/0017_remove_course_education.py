# Generated by Django 4.0.6 on 2022-12-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_experiences_projects_course_user_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='education',
        ),
    ]
