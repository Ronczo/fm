# Generated by Django 4.1.4 on 2022-12-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="Image",
            name="picture",
            field=models.FileField(blank=True, null=True, upload_to="pictures/"),
        ),
    ]
