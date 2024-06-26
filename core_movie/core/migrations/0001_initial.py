# Generated by Django 5.0.2 on 2024-05-01 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MPAA_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('imgPath', models.ImageField(upload_to='movie_images/')),
                ('duration', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=100)),
                ('userRating', models.CharField(max_length=10)),
                ('genre', models.ManyToManyField(to='core.genre')),
                ('mpaaRating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mpaa_rating')),
            ],
        ),
    ]
