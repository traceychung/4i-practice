from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import employee_to_dict


@csrf_exempt
@require_http_methods(["GET", "POST"])
def list_employees(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        data = list(employees.values())
        return JsonResponse(data, safe=False, status=200)
    else:
        data = json.loads(request.body)
        employee = Employee.objects.create(**data)
        data = list(Employee.objects.values())
        return JsonResponse(data, safe=False, status=200)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def get_employee(request, pk):
    if request.method == "GET":
        try:
            employee = Employee.objects.get(id=pk)
            employee_data = employee_to_dict(employee)
            return JsonResponse(employee_data, safe=False, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )
    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
            Employee.objects.filter(id=pk).update(**data)
            employee = Employee.objects.get(id=pk)
            employee_data = employee_to_dict(employee)
            return JsonResponse(employee_data, safe=False, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )
    else:
        try:
            employee = Employee.objects.get(id=pk)
            Employee.objects.filter(id=pk).delete()
            return JsonResponse(
                {"message": "Employee was deleted"},
                status=200,
            )
        except Employee.DoesNotExist:
            return JsonResponse({"message": "ID not found"}, safe=False, status=404)

        except Exception as e:
            return JsonResponse(
                {"message": f"An error occurred: {str(e)}"},
                status=500,
            )
