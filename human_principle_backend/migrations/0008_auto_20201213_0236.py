# Generated by Django 3.1.4 on 2020-12-13 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_principle_backend', '0007_auto_20201213_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='username',
            new_name='user_pk',
        ),
    ]
