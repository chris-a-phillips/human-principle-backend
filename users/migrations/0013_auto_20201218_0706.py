# Generated by Django 3.1.4 on 2020-12-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201217_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.CharField(max_length=255),
        ),
    ]