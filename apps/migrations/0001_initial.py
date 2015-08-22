# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'cars_images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'Clothes_images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClothesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'Electronic_images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ForHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'forHome_images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ForHomeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='forhome',
            name='name',
            field=models.ForeignKey(to='apps.ForHomeType'),
        ),
        migrations.AddField(
            model_name='electronic',
            name='name',
            field=models.ForeignKey(to='apps.ElectronicType'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='name',
            field=models.ForeignKey(to='apps.ClothesType'),
        ),
        migrations.AddField(
            model_name='cars',
            name='name',
            field=models.ForeignKey(to='apps.CarsType'),
        ),
    ]
