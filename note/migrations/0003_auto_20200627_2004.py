# Generated by Django 3.0.7 on 2020-06-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20200621_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(upload_to='note/static/img'),
        ),
    ]
