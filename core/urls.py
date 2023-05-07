from django.urls import path

from .views import about, index, pricing

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('pricing/', pricing, name="pricing"),
]