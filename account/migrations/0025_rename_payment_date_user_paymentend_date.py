# Generated by Django 4.0.6 on 2022-12-03 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_user_payment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='payment_date',
            new_name='paymentend_date',
        ),
    ]
