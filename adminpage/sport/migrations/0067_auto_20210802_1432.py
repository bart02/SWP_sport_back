# Generated by Django 3.1.8 on 2021-08-02 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0066_change_medical_reference_in_medical_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.sport'),
        ),
    ]
