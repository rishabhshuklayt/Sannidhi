from rest_framework import serializers

class CreateTenantSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True)
    domain = serializers.CharField(required=True, max_length=100)
    plan = serializers.CharField(required=True, max_length=100)
    tenant_type = serializers.CharField(required=True, max_length=100)
    metadata = serializers.JSONField(required=False, default=dict)
    private_metadata = serializers.JSONField(required=False, default=dict)
    is_active = serializers.BooleanField(required=False, default=True)
    is_exempted = serializers.BooleanField(required=False, default=False)