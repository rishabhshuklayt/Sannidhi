from django.urls import path

from apps.MultiTenants.views import CreateTenant

urlpatterns = [
    path('create-tenant/', CreateTenant.as_view(), name='create_tenant'),
    path('get-tenant/<int:tenant_id>/', CreateTenant.as_view(), name='get_tenant'),
   
]