# Generated by Django 4.0.6 on 2022-11-29 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='username',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='company',
            name='last_name',
        ),
    ]