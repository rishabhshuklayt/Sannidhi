from apps.geofence.models import Geofence
class GeofenceRepository:
    def create_geofence(self, name, latitude, longitude, radius):
        return Geofence.objects.create(name=name, latitude=latitude, longitude=longitude, radius=radius)

    def get_geofence_by_id(self, geofence_id):
        # Logic to retrieve geofence data from the database
        return Geofence.objects.get(id=geofence_id)
    
    def get_geofence_by_name(self, name):
        # Logic to retrieve geofence data from the database
        return Geofence.objects.get(name=name)
    
    def get_geofence_existance(self, name, latitude, longitude, radius):
        # Logic to retrieve geofence data from the database
       return Geofence.objects.filter(
           name=name,
           latitude=latitude,
           longitude=longitude,
           radius=radius
        ).exists()