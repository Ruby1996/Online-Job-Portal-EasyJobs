# Generated by Django 2.2.5 on 2019-11-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20191109_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='com_pro',
            name='comusername',
        ),
    ]
