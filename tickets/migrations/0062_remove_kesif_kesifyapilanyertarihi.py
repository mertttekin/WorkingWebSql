# Generated by Django 3.2.15 on 2022-10-17 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0061_kesif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kesif',
            name='kesifYapilanYerTarihi',
        ),
    ]
