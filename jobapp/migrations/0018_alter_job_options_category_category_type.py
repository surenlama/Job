# Generated by Django 4.0.6 on 2022-12-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_job_job_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='category',
            name='category_type',
            field=models.CharField(choices=[('Digital Work', 'digital'), ('Field Work', 'field')], default='digital', max_length=250),
        ),
    ]