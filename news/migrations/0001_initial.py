# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('addr', models.CharField(max_length=256, verbose_name=b'\xe7\xbd\x91\xe5\x9d\x80', db_index=True)),
                ('content', models.TextField(default=b'', verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('published', models.BooleanField(default=True, verbose_name=b'\xe6\xad\xa3\xe5\xbc\x8f\xe5\x8f\x91\xe5\xb8\x83')),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u6559\u7a0b',
                'verbose_name_plural': '\u6559\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('addr', models.CharField(max_length=256, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe7\xbd\x91\xe5\x9d\x80', db_index=True)),
                ('intro', models.TextField(default=b'', verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe7\xae\x80\xe4\xbb\x8b')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name=b'\xe5\xbd\x92\xe5\xb1\x9e\xe6\xa0\x8f\xe7\x9b\xae'),
        ),
    ]
