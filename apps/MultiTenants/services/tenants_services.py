

class tenantsServices:
    def __init__(self, tenant_repository, email_factory):
        self.tenants_repository = tenant_repository
        self.EmailFactory = email_factory

    def create_tenants(self, name, tenant_type, plan , email, domain, metadata, private_metadata, is_active, is_exempted):
        # Logic to create a new tenant
        return self.tenants_repository.create_tenant(
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

        
        pass

    def update_tenants(self, tenant_id, geofence_id, geofence_data):
        # Logic to update a specific geofence for the specified tenant
        pass

    def delete_tenants(self, tenant_id, geofence_id):
        # Logic to delete a specific geofence for the specified tenant
        pass

    def get_tenants(self, tenant_id):
        # Logic to retrieve all geofences for the specified tenant
        pass