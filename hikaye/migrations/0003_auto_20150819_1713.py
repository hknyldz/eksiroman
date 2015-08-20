# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0002_auto_20150819_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='hikaye',
            name='parent',
            field=models.ForeignKey(null=True, to='hikaye.Hikaye'),
        ),
        migrations.AlterField(
            model_name='hikaye',
            name='writer',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
