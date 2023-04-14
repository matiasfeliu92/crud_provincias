from django.contrib import admin
from .models import Cities, Provinces

class ProvincesModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'surface', 'population', 'density', 'region_id')

class CitiesModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'province_id')

admin.site.register(Provinces, ProvincesModelAdmin)
admin.site.register(Cities, CitiesModelAdmin)