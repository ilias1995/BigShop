# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20150820_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothes',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronic',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forhome',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
