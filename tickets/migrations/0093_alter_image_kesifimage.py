# Generated by Django 3.2.15 on 2022-10-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0092_auto_20221031_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='kesifImage',
            field=models.ImageField(blank=True, null=True, upload_to='Kesif/'),
        ),
    ]
