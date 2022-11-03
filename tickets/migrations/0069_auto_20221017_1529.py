# Generated by Django 3.2.15 on 2022-10-17 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0068_auto_20221017_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='KesifPTSMalzeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kesifKameraSayisi', models.IntegerField(default=0)),
                ('kesifDirekSayisi', models.IntegerField(default=0)),
                ('kesifAdaptorSayisi', models.IntegerField(default=0)),
                ('kesifDirekUzunlugu', models.IntegerField(default=1.5)),
                ('kesifSwitchTipi', models.CharField(max_length=25, null=True)),
                ('kesifSwitchSayisi', models.IntegerField(default=0)),
                ('kesifBigisayarConfigi', models.CharField(default='yok', max_length=100)),
                ('kesifIoKartTipi', models.CharField(default='yok', max_length=25)),
                ('kesifIoKartmodulaciklamasi', models.CharField(default='yok', max_length=50)),
                ('kesifIoKartSayisi', models.IntegerField(default=0)),
                ('kesifPanoTipi', models.CharField(max_length=50)),
                ('kesifPanoSayisi', models.IntegerField(default=0)),
                ('kesifCAT6kablometre', models.IntegerField(default=0)),
                ('kesifEnerjikablometre', models.IntegerField(default=0)),
                ('kesifDT8kablometre', models.IntegerField(default=0)),
                ('kesifSprellTipi', models.CharField(default='yok', max_length=25)),
                ('kesifSprellmetre', models.IntegerField(default=0)),
                ('kesifFiberVarMi', models.BooleanField(default=False)),
                ('kesifFiberMetre', models.IntegerField(default=0)),
                ('kesifPatchPanelTipi', models.CharField(max_length=25, null=True)),
                ('kesifPatchPanelSayisi', models.IntegerField(default=0)),
                ('kesifCibikModuleVarMi', models.BooleanField(default=False)),
                ('kesifCibikModuleSayisi', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='KesifMalzeme',
            new_name='KesifOlayMalzeme',
        ),
        migrations.RenameField(
            model_name='kesif',
            old_name='KesifMalzemeler',
            new_name='KesifOlayMalzemeler',
        ),
        migrations.AddField(
            model_name='kesif',
            name='KesifPTSMalzemeler',
            field=models.ForeignKey(blank=True, default=35, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.kesifptsmalzeme'),
        ),
    ]