from rest_framework.routers import DefaultRouter

from mainapp.views import UserViewSet


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns = []

urlpatterns += router.urls
