# Generated by Django 4.0.4 on 2022-06-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0032_remove_paylasim_göndericiuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='paylasim',
            name='göndericiUser',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
