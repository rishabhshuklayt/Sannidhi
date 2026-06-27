from django.shortcuts import render
from strawberry.test import Response

from apps.geofence.serlialziers.geofence_serializer import GeofenceSerializer
from apps.geofence.services.geofence_services import GeoFenceService
from apps.geofence.repository.geofence_repository import GeofenceRepository

# Create your views here.
from rest_framework.views import APIView
# path: apps/geofence/views.py

class GeofenceView(APIView):


    def post(self, request):
        # Logic to create a new geofence
        serializer = GeofenceSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        name = serializer.validated_data.get("name")
        latitude = serializer.validated_data.get("latitude")
        longitude = serializer.validated_data.get("longitude")
        radius = serializer.validated_data.get("radius")

        
        # logic for processing the geofence data and saving it to the database
        service = GeoFenceService(geofence_repository=GeofenceRepository())
        new_geofence = service.create_geofence( name, latitude, longitude, radius)

        if not new_geofence:
            return Response({
                "message": "Failed to create geofence"
            })
        
        return Response({
            "message": "Geofence created successfully",
            "geofence": {
                "id": new_geofence.id,
                "name": new_geofence.name,
                "latitude": new_geofence.latitude,
                "longitude": new_geofence.longitude,
                "radius": new_geofence.radius
            }
        }, status=201)

    # def get_geofence(self, request):
    #     # Logic to retrieve geofence data
    #     pass

    # def create_geofence(self, request):
    #     pass

    # def update_geofence(self, request, geofence_id):
    #     # Logic to update an existing geofence
    #     pass

    # def delete_geofence(self, request, geofence_id):
    #     # Logic to delete a geofence
    #     pass