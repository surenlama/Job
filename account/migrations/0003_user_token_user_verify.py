# Generated by Django 4.0.6 on 2022-11-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_experience_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='fref', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
