# Generated by Django 3.1.4 on 2020-12-15 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_principle_backend', '0011_auto_20201214_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principle',
            old_name='username',
            new_name='email',
        ),
    ]