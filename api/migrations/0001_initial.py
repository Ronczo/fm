# Generated by Django 4.1.4 on 2022-12-29 17:06

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("width", models.PositiveSmallIntegerField()),
                ("height", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
