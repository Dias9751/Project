# Generated by Django 2.2 on 2022-04-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='ph_restaurant',
            field=models.CharField(max_length=300),
        ),
    ]