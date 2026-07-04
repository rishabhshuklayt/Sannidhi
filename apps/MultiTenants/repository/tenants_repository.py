
from apps.MultiTenants.models import Tenants
from django.db.models import Q


class TenantsRepository:
    def __init__(self):
        pass

    def create_tenant(self, name, tenant_type, plan , email, domain, metadata, private_metadata, is_active, is_exempted):
        
      tenant = Tenants.objects.create(
        name=name,
        tenant_type=tenant_type,
        plan=plan,
        email=email,
        domain=domain,
        metadata=metadata,
        private_metadata=private_metadata,
        is_active=is_active,
        is_exempted=is_exempted
      )
      return tenant
    
    def get_tenant_by_email_or_domain(self, email, domain):
        
        return Tenants.objects.filter(
            Q(email=email) | Q(domain=domain)
        ).first()