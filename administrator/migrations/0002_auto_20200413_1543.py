# Generated by Django 2.2.5 on 2020-04-13 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpdesk',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='helpdesk',
            name='reply_date',
        ),
    ]