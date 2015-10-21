# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('social_id', models.TextField(default=b'')),
                ('social_alias', models.TextField(default=b'')),
                ('social_fist_name', models.TextField(default=b'')),
                ('social_last_name', models.TextField(default=b'')),
                ('social_email', models.TextField(default=b'')),
                ('social_gender', models.TextField(default=b'')),
                ('social_language', models.TextField(default=b'')),
                ('social_avatar', models.TextField(default=b'')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
