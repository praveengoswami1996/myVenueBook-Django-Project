# Generated by Django 4.0.1 on 2022-06-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customertable',
            old_name='customerMobile',
            new_name='customerMobileNumber',
        ),
        migrations.AddField(
            model_name='customertable',
            name='customerMobileCountryCode',
            field=models.CharField(default='', max_length=10),
        ),
    ]
