# Generated by Django 4.0.6 on 2022-12-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_user_apply_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apply_attempt',
            field=models.IntegerField(default=0),
        ),
    ]
