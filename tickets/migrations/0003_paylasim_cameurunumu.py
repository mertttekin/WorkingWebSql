# Generated by Django 4.0.4 on 2022-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_rename_göndericiaciklama_ariza_gelenaciklama_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paylasim',
            name='cameUrunumu',
            field=models.BooleanField(default=False),
        ),
    ]
