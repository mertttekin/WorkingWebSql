# Generated by Django 3.2.15 on 2022-10-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0075_alter_kesifptsmalzeme_kesifdirekuzunlugu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifDirekUzunlugu',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSyeradi',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
