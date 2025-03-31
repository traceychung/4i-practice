from django.urls import path
from . import views

urlpatterns = [
    path("all", views.list_assets),
    path("<int:pk>", views.get_asset)
]
