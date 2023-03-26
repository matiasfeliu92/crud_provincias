from rest_framework import serializers
from .models import Provinces

class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = ('id', 'name', 'surface', 'region')