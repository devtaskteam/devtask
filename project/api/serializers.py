from project.models import Project, Stage, Task
from authapp.models import User
from rest_framework import serializers


# class ProjectSerializer(serializers.ModelSerializer):
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:project-detail')
    users = serializers.HyperlinkedRelatedField(
        label='Ползователи',
        queryset=User.objects.all(),
        view_name='api:user-detail',
        many=True
    )

    class Meta:
        model = Project
        fields = '__all__'


class StageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:stage-detail')
    id_project = serializers.HyperlinkedRelatedField(
        label='Название проекта',
        queryset=Project.objects.all(),
        view_name='project:project-detail'
    )

    class Meta:
        model = Stage
        fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project:task-detail')
    id_project = serializers.HyperlinkedRelatedField(
        label='Название проекта',
        queryset=Project.objects.all(),
        view_name='project:project-detail'
    )

    id_stage = serializers.HyperlinkedRelatedField(
        label='Название этапа',
        queryset=Stage.objects.all(),
        view_name='project:stage-detail'
    )

    id_user = serializers.HyperlinkedRelatedField(
        label='Ползователи',
        queryset=User.objects.all(),
        view_name='api:user-detail'
    )

    class Meta:
        model = Task
        fields = '__all__'
