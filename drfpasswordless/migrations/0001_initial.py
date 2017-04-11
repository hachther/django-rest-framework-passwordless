# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 03:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import drfpasswordless.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('to_alias', models.CharField(blank=True, max_length=40)),
                ('to_alias_type', models.CharField(blank=True, max_length=20)),
                ('key', models.CharField(default=drfpasswordless.models.generate_numeric_token, max_length=6, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Callback Token',
                'abstract': False,
                'ordering': ['-id'],
                'get_latest_by': 'created_at',
            },
        ),
        migrations.AlterUniqueTogether(
            name='callbacktoken',
            unique_together=set([('key', 'is_active')]),
        ),
    ]