from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

from women.views import WomenAPIList, WomenAPIDestroy, WomenAPIUpdate
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Women API',
        description='Test description',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='sanjar.ravshanbekov@gmail.com'),
        license=openapi.License(name="Women project"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view(), name='women-list'),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')
]
