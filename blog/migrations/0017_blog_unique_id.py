# Generated by Django 3.0.4 on 2020-10-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20201023_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='unique_id',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
    ]
