from django.urls import path

from .views import dashboard

app_name = "appdashboard"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]