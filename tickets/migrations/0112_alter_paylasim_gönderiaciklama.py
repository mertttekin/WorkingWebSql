# Generated by Django 3.2.15 on 2022-11-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0111_kesif_kesifarsivmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='gönderiAciklama',
            field=models.TextField(),
        ),
    ]
