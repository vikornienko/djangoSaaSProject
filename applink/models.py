from django.db import models

from appaccounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, related_name="categories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Link(models.Model):
    category = models.ForeignKey(Category, related_name="links", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, related_name="links", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
