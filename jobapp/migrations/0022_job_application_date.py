# Generated by Django 4.0.6 on 2022-12-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0021_rename_vacancy_job_no_of_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='application_date',
            field=models.DateField(null=True),
        ),
    ]