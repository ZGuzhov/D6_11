# Generated by Django 3.1 on 2020-08-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200815_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, upload_to='books'),
        ),
    ]
