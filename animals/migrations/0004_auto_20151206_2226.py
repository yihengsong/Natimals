# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20151124_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natimal',
            name='model_pic1',
            field=models.ImageField(null=True, upload_to=b'animals/static/pic_folder/', blank=True),
        ),
        migrations.AlterField(
            model_name='natimal',
            name='model_pic2',
            field=models.ImageField(null=True, upload_to=b'animals/static/pic_folder/', blank=True),
        ),
    ]
