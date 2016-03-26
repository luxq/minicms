# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='update_time',
        ),
    ]
