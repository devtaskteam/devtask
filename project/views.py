from django_filters.rest_framework import DjangoFilterBackend
from project.api.serializers import ProjectSerializer, StageSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from project.models import Project, Stage, Task

from rest_framework import filters


class CustomProjectsSetPagination(PageNumberPagination):
    page_size = 18
    page_size_query_param = 'page_size'
    max_page_size = 18


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
    queryset = Project.objects.all().order_by('is_active', '-id')
    serializer_class = ProjectSerializer
    pagination_class = CustomProjectsSetPagination
    parser_classes = (MultiPartParser,)
    lookup_field = 'slug'

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('id_user__name',)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('users__id',)


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Project
    queryset = Project.objects.all().order_by('is_active', '-id')
    serializer_class = ProjectSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class StageList(generics.ListCreateAPIView):

    model = Stage
    queryset = Stage.objects.all().order_by('is_active', 'id')
    serializer_class = StageSerializer

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('id_project__id',)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id_project__id',)


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
    queryset = Task.objects.all().order_by('is_active', 'id')
    serializer_class = TaskSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id_project__id', 'id_user__id')


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Task
    queryset = Stage.objects.all()
    serializer_class = TaskSerializer
