# Generated by Django 3.2.15 on 2022-11-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0104_auto_20221108_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifPTSLoopDedektorSayisi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifPTSLoopKabloCesidi',
            field=models.CharField(blank=True, choices=[('0.75mm² NYAF', '0.75mm² NYAF'), ('1mm² NYAF', '1mm² NYAF'), ('1.5mm² NYAF', '1.5mm² NYAF'), ('2.5mm² NYAF', '2.5mm² NYAF')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifPTSLoopKabloMetresi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifPTSLoopTrafoSayisi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSMantarBariyerModeli',
            field=models.CharField(choices=[('2 li', '2 li'), ('3 lu', '3 lu'), ('4 lu', '4 lu'), ('5 li', '5 li'), ('6 li', '6 li')], default='yok', max_length=25),
        ),
    ]