# Generated by Django 3.1 on 2020-08-23 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200822_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
    ]
