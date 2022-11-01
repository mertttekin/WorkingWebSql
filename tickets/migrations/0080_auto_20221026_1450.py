# Generated by Django 3.2.15 on 2022-10-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0079_kesifptsmalzeme_kesifkameratipi'),
    ]

    operations = [
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifExtraKameraSayisi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifExtraKameraTipi',
            field=models.CharField(choices=[('IPC-HFW1431TP-ZS 4MP', 'IPC-HFW1431TP-ZS 4MP'), ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP')], default='---', max_length=25),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifKameraTipi',
            field=models.CharField(choices=[('IPC-HFW1431TP-ZS 4MP', 'IPC-HFW1431TP-ZS 4MP'), ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP')], default='---', max_length=25),
        ),
    ]
