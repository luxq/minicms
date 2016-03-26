# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160326_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
    ]
