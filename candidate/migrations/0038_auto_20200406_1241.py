# Generated by Django 2.2.5 on 2020-04-06 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0037_auto_20200405_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapply',
            name='canname',
        ),
        migrations.RemoveField(
            model_name='jobapply',
            name='comname',
        ),
        migrations.RemoveField(
            model_name='jobapply',
            name='job_name',
        ),
    ]
