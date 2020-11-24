from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import BaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'  # Exposes all fields of the model.


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
