# Generated by Django 2.2 on 2020-12-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0008_auto_20201227_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='unique_id',
            field=models.CharField(default='92271', max_length=10),
        ),
    ]
