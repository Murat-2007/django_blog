# Generated by Django 3.0.4 on 2020-10-30 20:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201029_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, verbose_name='İçerik'),
        ),
    ]
