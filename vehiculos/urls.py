from django.urls import path
from . import views

app_name = "vehiculos"

urlpatterns = [
    path("", views.index, name="index"),
    
    ]