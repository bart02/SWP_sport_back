# Generated by Django 3.0.5 on 2020-05-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0011_auto_20200502_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='special',
            field=models.BooleanField(default=False, verbose_name='Technical/Club only'),
        ),
    ]
