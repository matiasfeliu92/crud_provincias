from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "provinciasCrud"

urlpatterns = [
    path('', views.get_provinces, name='get_provinces'),
    path('cities', views.get_cities, name='get_cities'),
    path('regions', views.get_regions, name='get_regions'),
    path('<int:id>', views.get_one_province, name='get_one_province'),
    path('cities/<int:id>', views.get_one_city, name='get_one_city'),
    path('regions/<int:id>', views.get_one_region, name='get_one_region'),
    path('new_prov', views.post_new_province, name='post_new_province'),
]