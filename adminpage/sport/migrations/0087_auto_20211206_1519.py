# Generated by Django 3.1.8 on 2021-12-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0086_auto_20211206_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnesstestexercise',
            name='select',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fitnesstestexercise',
            name='value_unit',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]