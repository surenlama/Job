# Generated by Django 4.0.6 on 2022-12-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, default='anil.png', upload_to='profile'),
        ),
    ]
