# Generated by Django 4.1.4 on 2022-12-29 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_image_picture"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="picture",
            new_name="url",
        ),
    ]
