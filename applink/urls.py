from django.urls import path

from .views import categories, create_category, create_link, delete_category, delete_link,edit_category, edit_link,links

app_name = "applink"

urlpatterns = [
    path("", links, name="links"),
    path("<int:pk>/edit/", edit_link, name="edit_link"),
    path("<int:pk>/delete/", delete_link, name="delete_link"),
    path("create-link/", create_link, name="create_link"),
    path("categories/", categories, name="categories"),
    path("categories/<int:pk>/edit/", edit_category, name="edit_category"),
    path("categories/<int:pk>/delete/", delete_category, name="delete_category"),
    path("categories/create-category/", create_category, name="create_category"),
]