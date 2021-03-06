# Generated by Django 2.2.5 on 2020-04-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='helpdesk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_username', models.CharField(max_length=100)),
                ('can_uname', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('reply', models.TextField()),
                ('help_date', models.DateField()),
                ('reply_date', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
