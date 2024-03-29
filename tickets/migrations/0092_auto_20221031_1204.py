# Generated by Django 3.2.15 on 2022-10-31 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0091_auto_20221027_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kesifptsmalzeme',
            name='kesifPTSPanoTipi',
            field=models.CharField(choices=[('iç ortam ', 'iç ortam '), ('dış ortam', 'dış ortam')], default='yok', max_length=50),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kesifImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('aitKesif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.kesif')),
            ],
        ),
    ]
