# Generated by Django 4.1.7 on 2023-03-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinciasCrud', '0002_alter_provincias_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincias',
            name='surface',
            field=models.IntegerField(),
        ),
    ]
