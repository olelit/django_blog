# Generated by Django 3.0.7 on 2020-06-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200627_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(upload_to='note/'),
        ),
    ]
