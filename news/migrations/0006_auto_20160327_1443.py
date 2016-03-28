# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160327_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe6\x98\xbe\xe7\xa4\xba'),
        ),
        migrations.AddField(
            model_name='column',
            name='nav_display',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\x98\xbe\xe7\xa4\xba'),
        ),
    ]
