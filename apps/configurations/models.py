from django.db import models

from apps.MultiTenants.models import Tenants

# Create your models here.
class configurations(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    configurations = models.JSONField(blank=True, null=True)
    identifier = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE, related_name='configurations')

    def __str__(self):
        return self.name