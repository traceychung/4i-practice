from django.urls import path
from . import views

urlpatterns = [
    path("all", views.list_employees),
    path("create", views.create_employees),
    path("<int:pk>", views.get_employee),
    path("update/<int:pk>", views.update_employees)
]
