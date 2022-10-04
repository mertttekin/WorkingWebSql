# Generated by Django 4.0.5 on 2022-06-11 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0045_alter_ariza_firma_bilgi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ariza',
            name='firma_bilgi',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.firma'),
        ),
        migrations.AlterField(
            model_name='firma',
            name='FirmaName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]