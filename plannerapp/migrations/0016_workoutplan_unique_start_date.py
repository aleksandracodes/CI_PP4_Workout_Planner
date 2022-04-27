# Generated by Django 3.2 on 2022-04-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0015_alter_workoutplan_options'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='workoutplan',
            constraint=models.UniqueConstraint(fields=('user', 'first_day'), name='unique_start_date'),
        ),
    ]
