# Generated by Django 4.0.6 on 2022-12-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0008_remove_dashboard_name_dashboard_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
