# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('plain_text', models.TextField(null=True, blank=True)),
                ('html', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['template_name'],
            },
        ),
    ]
