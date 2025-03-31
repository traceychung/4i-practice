from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt

# View all
@require_http_methods("GET")
def list_employees(request):
    employees = Employee.objects.all()
    data = list(employees.values())
    return JsonResponse(data, safe=False)

# Create new
@csrf_exempt
@require_http_methods("POST")
def create_employees(request):
    data = json.loads(request.body)
    employee = Employee.objects.create(**data)
    data = list(Employee.objects.values())
    return JsonResponse(
        data,
        safe=False
    )

# Get by id
@require_http_methods("GET")
def get_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee_data = {
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'phone': employee.phone,
        'bio': employee.bio,
        'union_member': employee.union_member
    }
    return JsonResponse(employee_data, safe=False)

# Update
@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
def update_employees(request, pk):
    if request.method == "PUT":
        data = json.loads(request.body)
        Employee.objects.filter(id=pk).update(**data)
        employee = Employee.objects.get(id=pk)
        employee_data = {
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'phone': employee.phone,
        'bio': employee.bio,
        'union_member': employee.union_member
    }
        return JsonResponse(
                employee_data,
                safe=False
            )
    elif request.method == "DELETE":
        employee = Employee.objects.filter(id=pk).delete()
        return JsonResponse(
                {"message": "Employee was deleted"},
                status=400,
            )
