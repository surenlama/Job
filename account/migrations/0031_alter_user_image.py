# Generated by Django 4.0.6 on 2022-12-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_remove_user_apply_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]