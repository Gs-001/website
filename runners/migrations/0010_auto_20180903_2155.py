# Generated by Django 2.0.5 on 2018-09-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runners', '0009_auto_20180515_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
