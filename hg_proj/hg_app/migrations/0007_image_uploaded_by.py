# Generated by Django 2.2 on 2020-12-23 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hg_app', '0006_auto_20201221_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hg_app.User'),
        ),
    ]
