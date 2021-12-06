from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'client_name']
        # fields = '__all__'
        depth = 2
