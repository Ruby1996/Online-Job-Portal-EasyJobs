# Generated by Django 2.2.5 on 2020-03-18 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0034_jobpost_shrt_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='shrt_skill1',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='shrt_skill2',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='shrt_skill3',
        ),
    ]
