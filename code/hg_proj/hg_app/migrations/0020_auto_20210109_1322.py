# Generated by Django 2.2 on 2021-01-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0019_auto_20210109_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='unique_id',
            field=models.CharField(default='10329', max_length=10),
        ),
    ]
