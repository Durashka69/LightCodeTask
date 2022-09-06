from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.yasg import urlpatterns as docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title='Barter',
        default_version='v1',
        contact=openapi.Contact(email='gulyashshsh@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += docs_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
