# Generated by Django 2.2.5 on 2020-02-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0027_jobpost_shrtp_ten'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='shrtp_pg',
            field=models.FloatField(default=9.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='shrtp_tlw',
            field=models.FloatField(default=9.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='shrtp_ug',
            field=models.FloatField(default=9.0),
            preserve_default=False,
        ),
    ]