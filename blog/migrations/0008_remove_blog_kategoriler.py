# Generated by Django 3.0.4 on 2020-10-18 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_kategoriler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='kategoriler',
        ),
    ]
