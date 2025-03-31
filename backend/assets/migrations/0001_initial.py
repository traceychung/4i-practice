# Generated by Django 5.1.7 on 2025-03-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("asset_name", models.CharField(max_length=200)),
                ("serial_number", models.SmallIntegerField(max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("color", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=2000)),
                ("cert_req", models.BooleanField(default=False)),
            ],
        ),
    ]
