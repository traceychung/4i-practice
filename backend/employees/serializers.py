from django.core import serializers
from .models import Employee

def employee_to_dict(employee):
    employee_data = {
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'phone': employee.phone,
        'bio': employee.bio,
        'union_member': employee.union_member
    }
    return employee_data
