# Generated by Django 3.2.15 on 2022-11-21 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0114_auto_20221118_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kesifcctvmalzeme',
            name='kesifCCTVBariyerSayisi',
        ),
    ]
