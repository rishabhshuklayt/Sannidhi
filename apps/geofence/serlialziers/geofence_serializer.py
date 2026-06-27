
from rest_framework import serializers

class GeofenceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    radius = serializers.FloatField()