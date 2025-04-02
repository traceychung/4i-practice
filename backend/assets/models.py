from django.db import models


class Asset(models.Model):
    asset_name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    cert_req = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asset_name}"
