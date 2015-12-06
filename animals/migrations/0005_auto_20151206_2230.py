# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_auto_20151206_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natimal',
            name='model_pic1',
            field=models.ImageField(null=True, upload_to=b'pic_folder/', blank=True),
        ),
        migrations.AlterField(
            model_name='natimal',
            name='model_pic2',
            field=models.ImageField(null=True, upload_to=b'pic_folder/', blank=True),
        ),
    ]
