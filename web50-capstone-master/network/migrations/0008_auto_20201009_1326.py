# Generated by Django 2.2.12 on 2020-10-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20201009_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
