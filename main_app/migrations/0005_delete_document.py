# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]