# from django.contrib.auth.models import User, Group
from project.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="project:project-detail")

    class Meta:
        model = Project
        fields = '__all__'

