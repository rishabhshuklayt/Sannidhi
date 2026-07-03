from django.shortcuts import render
from rest_framework.views import APIView, Response

from apps.MultiTenants.serializers.createTenantSerializer import CreateTenantSerializer

# Create your views here.


class CreateTenant(APIView):
    """
    API view to create a new tenant.
    """
    def post(self, request, *args, **kwargs):
        # Logic to create a new tenant goes here
        serializer = CreateTenantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        email = serializer.validated_data.get("email")
        name = serializer.validated_data.get("name")
        domain = serializer.validated_data.get("domain")
        plan = serializer.validated_data.get("plan")
        tenant_type = serializer.validated_data.get("tenant_type")

        
        # Perform tenant creation logic here
        return Response({"message": "Tenant created successfully."}, status=201)
