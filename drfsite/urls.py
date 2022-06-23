from django.contrib import admin
from django.urls import path, include

from women.views import WomenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet,  basename='women')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
