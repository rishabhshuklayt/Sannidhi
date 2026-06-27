class GeoFenceService:
    def __init__(self, geofence_repository):
        self.geofence_repository = geofence_repository
    def create_geofence(self, name, latitude, longitude, radius):
        # Logic to create a new geofence
        if not name or not latitude or not longitude or not radius:
            raise ValueError("All fields are required")
        # check if geofence with the same name already exists
        if self.geofence_repository.get_geofence_existance(name, latitude, longitude, radius):
            raise ValueError("Geofence with the same name already exists")
        new_geofence = self.geofence_repository.create_geofence(name, latitude, longitude, radius)

        if not new_geofence:
            raise Exception("Failed to create geofence")
        
        return new_geofence

    def get_geofence(self):
        # Logic to retrieve geofence data
        pass