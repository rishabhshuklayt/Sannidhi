from django.shortcuts import render
from rest_framework.views import APIView, Response
from apps.MultiTenants.services.tenants_services import tenantsServices
# Create your views here.

class CreateConfigurationView(APIView):
    def post(self, request, *args, **kwargs):
        # Logic to create a new configuration goes here
        ####
       # I NEED TO ADDD THE MIDDLEWARE TO DO ALL CLIENT BASED STUFF DOIN IT IN EVERY CLASS IS NOT A GOOD APRRCOH SO I WILL ADD MIDDLEWARE FOR THAT AND ALSO ONE MROE THING I NEED TO ADD IS THE TENANT ID IN THE REQUEST HEADER SO THAT I CAN GET THE TENANT ID FROM THE HEADER AND THEN USE IT TO CREATE THE CONFIGURATION FOR THAT TENANT AND ADD THIS TO SELD AND ALSO ONE
       # MORE THING TAHT IS I NEED TO CACHE IT AS WELL SO IT SHOLD BE FAST OKAY OTEHRWISE ALL REQUEST WILL BE SLOW BUT I THINK IT WLL BE SLOW TOO WHAT TO DO NOW ??????? 
        tenant_id = request.data.get('tenant_id')
        tenant = tenantsServices.get_tenant_by_id(tenant_id)
        if not tenant:
            return Response({"error": "Tenant not found."}, status=404)
        # Additional logic for creating configuration
        return Response({"message": "Configuration created successfully."}, status=201)
    pass