
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'office', views.OfficeViewSet)
router.register(r'workplace_off', views.Workplace_offViewSet)
router.register(r'reserved', views.ReservedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('offices.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

