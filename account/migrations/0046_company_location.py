# Generated by Django 4.0.6 on 2022-12-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_user_hobby_user_whyneed'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
    ]