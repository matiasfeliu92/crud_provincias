import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework. response import Response

from provinciasCrud.serializers import ProvincesSerializer, RegionSerializer
from .models import Provinces, Region

# Create your views here.
class ProvincesViewSet(viewsets.ModelViewSet):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        province = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(province)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer