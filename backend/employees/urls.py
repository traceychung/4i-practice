from django.urls import path
from . import views

urlpatterns = [path("", views.list_employees), path("<int:pk>", views.get_employee)]
