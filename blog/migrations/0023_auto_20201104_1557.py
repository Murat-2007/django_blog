# Generated by Django 3.0.4 on 2020-11-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Yorumlar'},
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
