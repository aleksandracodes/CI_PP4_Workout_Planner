# Generated by Django 3.2 on 2022-04-05 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='plannerapp.workoutplan'),
        ),
    ]
