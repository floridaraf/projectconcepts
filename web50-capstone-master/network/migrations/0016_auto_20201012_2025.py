# Generated by Django 2.2.12 on 2020-10-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20201012_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pictures2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='pictures3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='pictures4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
