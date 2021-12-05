# Generated by Django 3.1.8 on 2021-08-08 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0073_make_hours_integer'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalgroupreference',
            name='student_comment',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name="Student's comment"),
        ),
        migrations.AddField(
            model_name='medicalgroupreference',
            name='uploaded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
