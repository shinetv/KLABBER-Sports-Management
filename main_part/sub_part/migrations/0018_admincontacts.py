# Generated by Django 3.2.3 on 2021-06-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0017_admincontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactmail', models.EmailField(max_length=254)),
                ('showmail', models.CharField(max_length=2)),
                ('contactPhone', models.CharField(max_length=15)),
                ('shownumber', models.CharField(max_length=15)),
                ('contactaddress', models.CharField(max_length=100)),
                ('showAddress', models.CharField(max_length=100)),
                ('sendmail', models.CharField(max_length=2)),
                ('adminstatus', models.CharField(max_length=2)),
                ('showDatabase', models.CharField(max_length=2)),
            ],
        ),
    ]
