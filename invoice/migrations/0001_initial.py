# Generated by Django 4.0.1 on 2022-06-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoiceTable',
            fields=[
                ('invoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('invoiceName', models.CharField(max_length=50)),
                ('invoiceAddress', models.CharField(max_length=120)),
                ('invoiceCity', models.CharField(max_length=50)),
                ('invoiceState', models.CharField(max_length=50)),
                ('invoicePincode', models.CharField(max_length=20)),
                ('venueParticular', models.CharField(max_length=250)),
                ('foodParticular', models.CharField(max_length=250)),
                ('danceFloorParticular', models.CharField(max_length=250)),
                ('venueParticularAmount', models.FloatField()),
                ('foodParticularAmount', models.FloatField()),
                ('danceFloorParticularAmount', models.FloatField()),
                ('invoiceTotalAmount', models.FloatField()),
                ('invoiceDate', models.DateField(auto_now_add=True)),
                ('bookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bookingtable')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customertable')),
            ],
        ),
    ]
