# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_natimal_model_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='natimal',
            old_name='model_pic',
            new_name='model_pic1',
        ),
        migrations.AddField(
            model_name='natimal',
            name='model_pic2',
            field=models.ImageField(null=True, upload_to=b'pic_folder/', blank=True),
        ),
    ]
