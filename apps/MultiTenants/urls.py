from django.urls import path

from apps.MultiTenants.views import CreateTenant

urlpatterns = [
    path('create-tenant/', CreateTenant.as_view(), name='create_tenant'),
]