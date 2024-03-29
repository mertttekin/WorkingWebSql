# Generated by Django 3.2.15 on 2022-10-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0089_kesifptsmalzeme_kesifptsiokartadaptorsayısı'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kesifptsmalzeme',
            old_name='kesifPTSSprellmetre',
            new_name='kesifPTSSpiralMetre',
        ),
        migrations.RenameField(
            model_name='kesifptsmalzeme',
            old_name='kesifPTSSprellTipi',
            new_name='kesifPTSSpiralÇapı',
        ),
        migrations.AddField(
            model_name='kesifptsmalzeme',
            name='kesifPTSEnerjikabloTipi',
            field=models.CharField(choices=[('3x1.5 TTR', '3x1.5 TTR'), ('3x2.5 TTR', '3x2.5 TTR'), ('2x1.5 TTR', '2x1.5 TTR')], default='yok', max_length=50),
        ),
    ]
