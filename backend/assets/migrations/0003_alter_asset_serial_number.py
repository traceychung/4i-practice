# Generated by Django 5.1.7 on 2025-03-31 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assets", "0002_alter_asset_serial_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="serial_number",
            field=models.CharField(max_length=50),
        ),
    ]
