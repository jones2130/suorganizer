# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='blog_posts', to='organizer.Tag'),
        ),
    ]