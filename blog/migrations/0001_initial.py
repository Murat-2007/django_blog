# Generated by Django 3.0.4 on 2020-09-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Baslik bilgisi buraya girilir', max_length=100, null=True, verbose_name='Baslik Giriniz')),
                ('icerik', models.TextField(max_length=1000, null=True, verbose_name='Icerik Giriniz')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
