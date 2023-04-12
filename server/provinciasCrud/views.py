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
from .models import Provinces, Region, Cities

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
    
@csrf_exempt
def post_new_province(request):
    regions = Region.objects.all()
    regionn = None
    id_region = None
    if request.method == 'POST':
        new_province = json.loads(request.body)
        print(new_province)
        for region in regions:
            if new_province['region_id'] == region.name:
                regionn = Region.objects.get(id=region.id)
                id_region = regionn
        print(id_region)
        province = Provinces(name=new_province['name'], surface=new_province['surface'], region_id=regionn, population=new_province['population'], density= new_province['density'])
        province.save()
    return HttpResponse('new province created', status=200)