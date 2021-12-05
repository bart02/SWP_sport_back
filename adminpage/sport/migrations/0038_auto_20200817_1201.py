# Generated by Django 3.0.7 on 2020-08-17 09:01

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0037_medicalgroupreference_semester'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='semester',
            name='semester_start_before_end',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='choice_deadline',
        ),
        migrations.AddConstraint(
            model_name='semester',
            constraint=models.CheckConstraint(check=models.Q(start__lte=django.db.models.expressions.F('end')), name='semester_start_before_end'),
        ),
    ]
