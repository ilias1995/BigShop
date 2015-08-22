# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20150820_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to=b'for_car')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type_for_car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='form_car',
            name='type',
            field=models.ForeignKey(to='apps.Type_for_car'),
        ),
    ]
