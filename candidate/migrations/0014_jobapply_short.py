# Generated by Django 2.2.5 on 2020-02-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0013_auto_20200216_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='short',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]