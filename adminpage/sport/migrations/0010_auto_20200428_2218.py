# Generated by Django 3.0.5 on 2020-04-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0009_auto_20200418_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='is_primary',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='GroupRequest',
        ),
    ]