# Generated by Django 3.0.5 on 2020-04-14 15:51

from django.db import migrations, models
import sport.models.attendance


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0005_student_is_ill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='hours',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[sport.models.attendance.validate_hours]),
        ),
    ]
