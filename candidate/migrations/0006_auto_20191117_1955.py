# Generated by Django 2.2.5 on 2019-11-17 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_jobapply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapply',
            old_name='com_uname',
            new_name='comname',
        ),
    ]