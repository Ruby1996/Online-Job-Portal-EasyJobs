# Generated by Django 2.2.5 on 2020-05-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0045_jobpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_pro',
            name='logo',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
