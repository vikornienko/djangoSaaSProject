from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from applink.models import Link


@login_required
def dashboard(request):
    links = Link.objects.filter(created_by=request.user)[:5]
    return render(request, "appdashboard/dashboard.html", {"links": links})
