from rest_framework import routers
from provinciasCrud.views import ProvincesViewSet, RegionViewSet

router = routers.DefaultRouter()

router.register('provinces', ProvincesViewSet, 'provinces_routes')
router.register('region', RegionViewSet, 'region_routes')

urlpatterns = router.urls