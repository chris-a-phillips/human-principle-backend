# Generated by Django 3.1.4 on 2020-12-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_principle_backend', '0013_auto_20201215_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principle',
            old_name='username',
            new_name='email',
        ),
    ]