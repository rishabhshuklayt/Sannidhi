from django.shortcuts import render
from rest_framework.views import APIView, Response
from apps.MultiTenants.services.tenants_services import tenantsServices
from apps.MultiTenants.repository.tenants_repository import TenantsRepository

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
       
        services = tenantsServices(
            tenant_repository = TenantsRepository
            
        )
        # send data to the service layer for tenant creation
        tenant = services.create_tenant(**serializer.validated_data)

        # Perform tenant creation logic here
        return Response({"message": "Tenant created successfully."}, status=201)
