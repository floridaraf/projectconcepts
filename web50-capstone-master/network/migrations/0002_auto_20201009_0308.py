# Generated by Django 2.2.12 on 2020-10-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
