# Generated by Django 2.2.5 on 2020-02-12 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0029_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='shrt_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
