# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0003_auto_20150819_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikaye',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, default=None, to='hikaye.Hikaye'),
        ),
    ]
