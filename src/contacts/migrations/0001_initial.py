# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-20 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_django', '0008_partial_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_id', models.PositiveIntegerField(db_index=True, default=0, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('user_social_auth',
                 models.ForeignKey(
                     default=0,
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='friends',
                     to='social_django.UserSocialAuth')),
            ],
        ),
    ]
