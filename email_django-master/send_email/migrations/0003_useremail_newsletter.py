# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0002_useremail_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremail',
            name='newsletter',
            field=models.BooleanField(default=True),
        ),
    ]