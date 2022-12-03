# Generated by Django 4.0.6 on 2022-12-03 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_category_post_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='cv',
        ),
        migrations.CreateModel(
            name='CVUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(null=True, upload_to='media')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
            ],
        ),
    ]
