# Generated by Django 3.1.4 on 2020-12-13 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_principle_backend', '0006_auto_20201213_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principle',
            old_name='questionnare_type',
            new_name='questionnaire_type',
        ),
    ]
