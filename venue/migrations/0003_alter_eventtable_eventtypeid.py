# Generated by Django 4.0.1 on 2022-06-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0002_remove_venuetable_venuecontact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtable',
            name='eventTypeId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]