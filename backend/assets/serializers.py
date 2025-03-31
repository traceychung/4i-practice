from django.core import serializers
from .models import Asset


def asset_to_dict(asset):
    data = {
        "asset_name": asset.asset_name,
        "serial_number": asset.serial_number,
        "price": asset.price,
        "color": asset.color,
        "description": asset.description,
        "cert_req": asset.cert_req,
    }
    return data
