# Generated by Django 2.2.12 on 2020-10-12 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20201012_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(upload_to='upload/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='network.Post')),
            ],
        ),
    ]
