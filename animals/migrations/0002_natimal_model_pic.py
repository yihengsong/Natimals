# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='natimal',
            name='model_pic',
            field=models.ImageField(null=True, upload_to=b'pic_folder/', blank=True),
        ),
    ]
