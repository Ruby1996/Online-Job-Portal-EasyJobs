# Generated by Django 2.2.5 on 2020-04-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_auto_20200413_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_username', models.CharField(max_length=100)),
                ('can_uname', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('reply_date', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
