# Generated by Django 3.1 on 2020-09-05 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
