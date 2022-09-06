from rest_framework import serializers

from mainapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login')

        """
        if we will count that the worker came to work as fact that he logged in,
        then we can just return the time when he last logged in.
        """
