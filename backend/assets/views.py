from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpRequest
from .models import Asset
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import asset_to_dict


@csrf_exempt
@require_http_methods(["GET", "POST"])
def list_assets(request: HttpRequest):
    if request.method == "GET":
        assets = Asset.objects.all()
        data = list(assets.values())
        return JsonResponse(data, safe=False, status=200)
    else:
        data = json.loads(request.body)
        new_asset = Asset.objects.create(**data)
        data = asset_to_dict(new_asset)
        return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def get_asset(request: HttpRequest, pk: int):
    if request.method == "GET":
        try:
            asset = Asset.objects.get(id=pk)
            data = asset_to_dict(asset)
            return JsonResponse(data, safe=False, status=200)
        except Asset.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            Asset.objects.filter(id=pk).update(**data)
            asset = Asset.objects.get(id=pk)
            data = asset_to_dict(asset)
            return JsonResponse(data, safe=False, status=200)
        except Asset.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )
    else:
        try:
            asset = Asset.objects.get(id=pk)
            Asset.objects.filter(id=pk).delete()
            return JsonResponse(
                {"message": "Asset was successfully deleted"}, safe=False
            )
        except Asset.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )
