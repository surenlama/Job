# Generated by Django 4.0.6 on 2022-12-04 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_alter_user_apply_attempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='apply_attempt',
        ),
    ]
