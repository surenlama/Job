# Generated by Django 4.0.6 on 2022-12-03 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_remove_job_cv_cvupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvupload',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cvjob', to='jobapp.job'),
        ),
    ]
