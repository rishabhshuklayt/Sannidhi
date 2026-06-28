from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class BaseTenantView(APIView):
    def dispatch(self, request, *args, **kwargs):
        # here i will write the Validations and permissions checks
        return super().dispatch(request, *args, **kwargs)
    pass

class CreateTenant(BaseTenantView):
    # here i will write buisnedd logic 
    pass