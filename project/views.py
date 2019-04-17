from project.api.serializers import ProjectSerializer, StageSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from project.models import Project, Stage, Task

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework


@api_view(['GET'])
def api_root(request):

    return Response({
        'projects': reverse('project:project-list', request=request),
        'stages': reverse('project:stage-list', request=request),
        'tasks': reverse('project:task-list', request=request),
        'main': reverse('api:user-list', request=request),

    })


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class ProjectList(generics.ListCreateAPIView):

    model = Project
    queryset = Project.objects.all().order_by('is_active', 'name')
    serializer_class = ProjectSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Project
    queryset = Project.objects.all().order_by('is_active', 'name')
    serializer_class = ProjectSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class StageList(generics.ListCreateAPIView):

    model = Stage
    queryset = Stage.objects.all().order_by('is_active', 'name')
    serializer_class = StageSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['id_project__id']


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class StageDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Stage
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class TaskList(generics.ListCreateAPIView):

    model = Task
    queryset = Task.objects.all().order_by('is_active', 'name')
    serializer_class = TaskSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['id_project__id']


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Task
    queryset = Stage.objects.all()
    serializer_class = TaskSerializer
