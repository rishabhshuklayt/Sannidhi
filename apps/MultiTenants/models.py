import uuid

from django.db import models

# Create your models here.
class Tenants(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, unique=True)
    client_uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(max_length=100, unique=True)
    metadata = models.JSONField(blank=True, null=True)
    plan = models.CharField(max_length=100, null=True)
    tenant_type = models.CharField(max_length=100,null=True)
    private_metadata = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_exempted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name