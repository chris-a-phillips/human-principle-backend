# Generated by Django 3.1.4 on 2020-12-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_principle_backend', '0008_auto_20201213_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principle',
            name='question_five',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_four',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_one',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_seven',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_six',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_three',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
        migrations.AlterField(
            model_name='principle',
            name='question_two',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='4', max_length=1),
        ),
    ]