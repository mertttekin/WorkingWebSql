# Generated by Django 4.0.5 on 2022-06-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0056_remove_ariza_arizacozumu_ariza_cozumvarmı_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ariza',
            name='gelenTelefon',
            field=models.CharField(max_length=11),
        ),
    ]
