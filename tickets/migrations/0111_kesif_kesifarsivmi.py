# Generated by Django 3.2.15 on 2022-11-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0110_auto_20221118_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='kesif',
            name='kesifArsivMi',
            field=models.BooleanField(default=False),
        ),
    ]