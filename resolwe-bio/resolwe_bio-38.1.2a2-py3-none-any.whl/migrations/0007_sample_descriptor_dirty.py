# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resolwe_bio", "0006_alter_versionfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="sample",
            name="descriptor_dirty",
            field=models.BooleanField(default=False),
        ),
    ]
