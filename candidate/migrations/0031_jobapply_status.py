# Generated by Django 2.2.5 on 2020-03-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0030_auto_20200318_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
