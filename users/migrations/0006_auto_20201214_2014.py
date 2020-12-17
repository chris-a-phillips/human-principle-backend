# Generated by Django 3.1.4 on 2020-12-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default='alpha', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.CharField(default='alpha', max_length=255),
            preserve_default=False,
        ),
    ]
