# Generated by Django 2.2.5 on 2020-03-21 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0031_jobapply_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapply',
            name='call',
        ),
        migrations.RemoveField(
            model_name='jobapply',
            name='call_date',
        ),
        migrations.RemoveField(
            model_name='jobapply',
            name='intw_desc',
        ),
    ]