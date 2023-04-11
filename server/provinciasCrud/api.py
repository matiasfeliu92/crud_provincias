from .models import Provinces
from rest_framework import viewsets, permissions
from .serializers import ProvincesSerializer

class ProvincesViewSet(viewsets.ModelViewSet):
    queryset = Provinces.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProvincesSerializer