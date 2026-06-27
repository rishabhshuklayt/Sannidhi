
from apps.geofence.views import GeofenceView
from django.urls import path

urlpatterns = [
    path('geofences/', GeofenceView.as_view(), name='geofence-list'),
    path('geofences/<str:name>/', GeofenceView.as_view(), name='geofence-detail'),
]