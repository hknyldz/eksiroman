# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hikaye',
            name='director',
        ),
        migrations.RemoveField(
            model_name='hikaye',
            name='writer',
        ),
        migrations.AddField(
            model_name='hikaye',
            name='writer',
            field=models.ForeignKey(to='hikaye.Hikaye', null=True),
        ),
    ]
