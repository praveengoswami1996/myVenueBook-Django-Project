# Generated by Django 4.0.1 on 2022-07-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_feedbacktable_feedbackresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertable',
            name='customerDob',
            field=models.DateField(null=True),
        ),
    ]
