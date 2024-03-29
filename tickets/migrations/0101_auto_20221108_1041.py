# Generated by Django 3.2.15 on 2022-11-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0100_alter_kesifptsmalzeme_kesifptskamerasayisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSExtraKameraAdaptorSayisi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSKameraAdaptorSayisi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSKameraBoatSayisi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSKameraTipi',
            field=models.CharField(blank=True, choices=[('yok', 'yok'), ('IPC-HFW1431TP-ZS 4MP', 'IPC-HFW1431TP-ZS 4MP'), ('IPC-HFW5231EP-Z 2MP', 'IPC-HFW5231EP-Z 2MP'), ('Muhafazalı Set (Box)', 'Muhafazalı Set (Box)')], max_length=25, null=True),
        ),
    ]
