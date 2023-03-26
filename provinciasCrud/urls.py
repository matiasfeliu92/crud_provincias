# from rest_framework import routers
# from provinciasCrud.api import ProvinciasViewSet

# router = routers.DefaultRouter()

# router.register('api/provincias', ProvinciasViewSet, 'provincias')

# urlpatterns = router.urls

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('provinces', views.get_provinces, name='get_all_provinces'),
    path('province/<int:id>', views.get_province, name='get_one_province'),
    path('new_province', views.post_new_province, name='post_new_province'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)