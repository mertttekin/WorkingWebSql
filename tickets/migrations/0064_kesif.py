# Generated by Django 3.2.15 on 2022-10-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0063_delete_kesif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kesif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kesifYapilanYerAdi', models.CharField(max_length=50)),
                ('kesifYapanKisi', models.CharField(max_length=50)),
                ('kesifSenaryosu', models.TextField(max_length=2000)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]
