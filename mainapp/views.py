from rest_framework.viewsets import ReadOnlyModelViewSet

from mainapp.serializers import UserSerializer
from mainapp.models import User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
