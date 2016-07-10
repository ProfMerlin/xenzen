# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xenserver', '0005_auto_20160624_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='xenvm',
            name='pvtip',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
