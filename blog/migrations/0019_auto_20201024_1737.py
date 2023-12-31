# Generated by Django 3.0.4 on 2020-10-24 14:37

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20201023_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='yayin_taslak',
            field=models.CharField(choices=[('yayin', 'YAYIN'), ('taslak', 'TASLAK')], default='yayin', max_length=6),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='default/default-photo.webp', help_text='Kapak Fotoğrafı Yükleyınız', null=True, upload_to=blog.models.upload_to, verbose_name='Resim'),
        ),
    ]
