# Generated by Django 2.2.5 on 2020-03-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0017_jobapply_short_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='intw_desc',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
