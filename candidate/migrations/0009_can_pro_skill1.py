# Generated by Django 2.2.5 on 2020-02-10 04:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0008_jobapply_canname'),
    ]

    operations = [
        migrations.AddField(
            model_name='can_pro',
            name='skill1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
