from rest_framework import serializers
from .models import Provinces, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

class ProvincesSerializer(serializers.ModelSerializer):
    region_id = RegionSerializer()
    class Meta:
        model = Provinces
        fields = ('id', 'name', 'surface', 'region_id')