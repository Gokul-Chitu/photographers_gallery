# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_post_model_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='model_pic',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.FileField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
