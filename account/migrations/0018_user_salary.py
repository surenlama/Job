# Generated by Django 4.0.6 on 2022-12-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_remove_course_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salary',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
