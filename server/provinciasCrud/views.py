from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404, JsonResponse
from rest_framework import viewsets, status
from rest_framework. response import Response
import json

from provinciasCrud.serializers import ProvincesSerializer, RegionSerializer
from .models import Provinces, Region, Cities

# Create your views here.
# class ProvincesViewSet(viewsets.ModelViewSet):
#     queryset = Provinces.objects.all()
#     serializer_class = ProvincesSerializer

#     def retrieve(self, request, pk=None):
#         queryset = self.get_queryset()
#         province = get_object_or_404(queryset, pk=pk)
#         serializer = self.get_serializer(province)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class RegionViewSet(viewsets.ModelViewSet):
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer

def get_provinces(request):
    provinces = Provinces.objects.all().values()
    return JsonResponse([dict(row) for row in provinces.values()], safe=False)

def get_cities(request):
    cities = Cities.objects.all().values()
    return JsonResponse([dict(row) for row in cities.values()], safe=False)

def get_regions(request):
    regions = Region.objects.all().values()
    return JsonResponse([dict(row) for row in regions.values()], safe=False)

def get_one_region(request, id):
    try:
        region = Region.objects.get(pk=id)
        data = {
            'name': region.name,
        }
        return JsonResponse(data, safe=False)
    except:
        return HttpResponse('region not found', status=404)

def get_one_province(request, id):
    try:
        province = Provinces.objects.get(pk=id)
        data = {
            'name': province.name,
            'surface': province.surface,
            'region': province.region_id
        }
        return JsonResponse(data, safe=False)
    except:
        return HttpResponse('province not found', status=404)
    
def get_one_city(request, id):
    try:
        city = Cities.objects.get(pk=id)
        data = {
            'name': city.name,
            'population': city.population,
            'province_id': city.province_id
        }
        return JsonResponse(data, safe=False)
    except:
        return HttpResponse('city not found', status=404)
    
def post_new_province(request):
    if request.method == 'POST':
        new_province = json.loads(request.body)