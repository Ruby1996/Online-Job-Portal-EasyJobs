# Generated by Django 2.2.5 on 2019-11-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20191116_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='com_username',
            field=models.CharField(max_length=250),
        ),
    ]
