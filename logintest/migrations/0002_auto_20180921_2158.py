# Generated by Django 2.1.1 on 2018-09-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logintest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='user_pw',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
