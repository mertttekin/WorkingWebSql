# Generated by Django 3.2.15 on 2022-11-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0098_alter_kesifptsmalzeme_kesifptsyeradi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSKameraSayisi',
            field=models.IntegerField(null=True),
        ),
    ]
