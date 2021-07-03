# Generated by Django 3.2.3 on 2021-06-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0014_auto_20210617_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manualbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches', models.CharField(max_length=12)),
                ('customername', models.CharField(max_length=100)),
                ('customerid', models.CharField(max_length=100)),
                ('customerPhoneNo', models.CharField(max_length=15)),
                ('customeraddress', models.CharField(max_length=1000)),
                ('ticketcount', models.CharField(max_length=1000)),
                ('bookingperson', models.CharField(max_length=100)),
                ('paymentamount', models.CharField(max_length=100000)),
                ('status', models.CharField(max_length=12)),
                ('confirmation', models.CharField(max_length=2)),
            ],
        ),
    ]