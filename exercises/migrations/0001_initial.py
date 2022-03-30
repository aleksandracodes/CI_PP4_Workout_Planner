# Generated by Django 3.2 on 2022-03-30 16:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('equipment', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('body_part', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
    ]
