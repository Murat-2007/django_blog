# Generated by Django 3.0.4 on 2020-10-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_kategoriler'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='kategoriler',
            field=models.ManyToManyField(null=True, to='blog.Kategori'),
        ),
    ]