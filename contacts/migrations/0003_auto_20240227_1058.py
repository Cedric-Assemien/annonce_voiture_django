# Generated by Django 3.0.7 on 2024-02-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20240226_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
