# Generated by Django 3.2.3 on 2021-06-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_profileu'),
    ]

    operations = [
        migrations.CreateModel(
            name='membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.CharField(max_length=100)),
                ('subdate', models.DateField()),
            ],
        ),
    ]
