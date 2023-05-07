from django.urls import path

from .views import create_category, create_link, links

app_name = "applink"

urlpatterns = [
    path("", links, name="links"),
    path("create-category/", create_category, name="create_category"),
    path("create-link/", create_link, name="create_link"),

]