# Generated by Django 3.2.3 on 2021-06-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0021_addmembership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='Planname',
            field=models.CharField(max_length=100),
        ),
    ]
