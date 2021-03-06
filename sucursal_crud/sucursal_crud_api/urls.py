from django.conf.urls import url
from django.urls import path, register_converter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
import sucursal_crud_api.views as views

schema_view = get_schema_view(
   openapi.Info(
      title="Sucursal API",
      default_version='v1',
      description="sucursal api description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sucursal/<int:id>/', views.SucursalDetailAPIView.as_view()),
    path('sucursal/', views.SucursalAPIView.as_view()),
    path('puntoDeRetiro/', views.PuntoDeRetiroAPIView.as_view()),
    path('puntoDeRetiro/<int:id>/', views.PuntoDeRetiroDetailAPIView.as_view()),
    path('nodo/', views.NodeAPIView.as_view()),
    path('nodo/cercano/<lat>/<lng>/', views.NearNodeAPIView.as_view())
]

