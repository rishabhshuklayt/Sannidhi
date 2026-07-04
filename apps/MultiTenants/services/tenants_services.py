
from cross_web import Response
class tenantsServices:
    def __init__(self, tenant_repository):
        self.tenants_repository = tenant_repository
        # self.EmailFactory = email_factory

    def create_tenant(self, name, tenant_type, plan , email, domain, metadata, private_metadata, is_active, is_exempted):
        # checking existing tenant with the same email or domain
        existing_tenant = self.tenants_repository.get_tenant_by_email_or_domain(self ,email, domain)
        if existing_tenant:
            return Response({"error": "Tenant with the same email or domain already exists."}, status=400)  # i should use exception here instead of response but for now i will use response
        # Logic to create a new tenant
        new_tenant = self.tenants_repository.create_tenant(self,
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
        
        #validating new tenant creation and sending email
        if not new_tenant:
            return None  
        return new_tenant
   

    def update_tenants(self, tenant_id, geofence_id, geofence_data):
        # Logic to update a specific geofence for the specified tenant
        pass

    def delete_tenants(self, tenant_id, geofence_id):
        # Logic to delete a specific geofence for the specified tenant
        pass

    def get_tenants(self, tenant_id):
        # Logic to retrieve all geofences for the specified tenant
        pass