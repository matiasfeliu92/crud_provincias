import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, Http404, JsonResponse
from .models import Provinces

# Create your views here.
@csrf_exempt
def get_provinces(request):
    provinces = Provinces.objects.all().values()
    return JsonResponse([dict(row) for row in provinces], safe=False)

@csrf_exempt
def get_province(request, id):
    province = Provinces.objects.get(id=id)
    province_dict = model_to_dict(province)
    return JsonResponse([province_dict], safe=False)

@csrf_exempt
def post_new_province(request):
    if request.method == 'POST':
        province = json.loads(request.body)
        print({'name': province['name']})
        new_province = Provinces(name=province['name'], surface=province['surface'])
        new_province.save()
    return JsonResponse({'message': 'new province inserted'})