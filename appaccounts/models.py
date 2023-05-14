from django.contrib.auth.models import AbstractUser
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=64)
    max_num_links = models.PositiveIntegerField()

class CustomUser(AbstractUser):
    plan = models.ForeignKey(Plan, related_name="users", on_delete=models.CASCADE)

