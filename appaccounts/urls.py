from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from .views import signup

app_name = "appaccounts"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", LoginView.as_view(template_name="appaccounts/login.html", form_class=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]