from .models import Client
from rest_framework import serializers
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']
        depth = 2
