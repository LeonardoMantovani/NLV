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
            name='Videogame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=10)),
                ('cover', models.ImageField(default='covers/no-image.png', upload_to='covers/')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
