# Generated by Django 3.2.15 on 2022-10-19 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0073_alter_kesifptsmalzeme_kesifdirekuzunlugu'),
    ]

    operations = [
        migrations.AddField(
            model_name='kesif',
            name='kesifYapilanYerTarihi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
