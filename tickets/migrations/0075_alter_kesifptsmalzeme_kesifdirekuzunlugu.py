# Generated by Django 3.2.15 on 2022-10-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0074_kesif_kesifyapilanyertarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifDirekUzunlugu',
            field=models.CharField(default='1,5 metre', max_length=25),
        ),
    ]
