# Generated by Django 2.2.5 on 2020-02-10 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0009_can_pro_skill1'),
    ]

    operations = [
        migrations.AddField(
            model_name='can_pro',
            name='skill2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='can_pro',
            name='skill3',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
