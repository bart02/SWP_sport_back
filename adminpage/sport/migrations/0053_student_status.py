# Generated by Django 3.1.8 on 2021-06-16 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0052_migrate_self_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'student statuses',
                'db_table': 'student_status',
            },
        ),
        migrations.RunSQL('''
        INSERT INTO student_status (id, name, description) VALUES 
        (0, 'Normal', 'Everything is ok'),
        (1, 'Dropped', 'Sorry, you are dropped'),
        (2, 'Academic leave', 'You are on academic leave'),
        (3, 'Alumnus', 'Congratulations, you are graduated!');
        ''', '')
    ]
