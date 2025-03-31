from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Asset
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import asset_to_dict

# Create your views here.
@csrf_exempt
@require_http_methods(["GET","POST"])
def list_assets(request):
    if request.method == "GET":
        assets = Asset.objects.all()
        data = list(Asset.objects.values())
        return JsonResponse(data, safe=False, status=200)
    else:
        data = json.loads(request.body)
        new_asset = Asset.objects.create(**data)
        data = list(Asset.objects.values())
        return JsonResponse(data, safe=False, status=200)

@csrf_exempt
@require_http_methods(["GET","PUT","DELETE"])
def get_asset(request, pk):
    if request.method == "GET":
        try:
            asset = Asset.objects.get(id=pk)
            data = asset_to_dict(asset)
            return JsonResponse(data, safe=False, status=200)
        except:
            return JsonResponse({"message": "ID does not exist"}, safe=False, status=404)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            update_asset = Asset.objects.filter(id=pk).update(**data)
            asset = Asset.objects.get(id=pk)
            data = asset_to_dict(asset)
            return JsonResponse(data, safe=False, status=200)
        except:
            return JsonResponse({"message": "ID does not exist"}, safe=False, status=404)
    else:
        try:
            asset = Asset.objects.get(id=pk)
            Asset.objects.filter(id=pk).delete()
            return JsonResponse({"message": "Asset was successfully deleted"}, safe=False)
        except:
            return JsonResponse({"message": "ID does not exist"}, safe=False, status=404)
