# Generated by Django 3.2.3 on 2021-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=100)),
                ('mailid', models.EmailField(max_length=254)),
                ('txtarea', models.CharField(max_length=1000)),
            ],
        ),
    ]
