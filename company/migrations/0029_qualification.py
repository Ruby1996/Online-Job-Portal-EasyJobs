# Generated by Django 2.2.5 on 2020-02-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0028_auto_20200211_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_username', models.CharField(max_length=100)),
                ('com_quali', models.CharField(max_length=100)),
            ],
        ),
    ]
