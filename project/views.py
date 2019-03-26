from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from project.api.serializers import ProjectSerializer, StageSerializer, TaskSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from project.models import Project, Stage, Task


@api_view(['GET'])
def api_root(request):

    return Response({
        'projects': reverse('project:project-list', request=request),
        'stages': reverse('project:stage-list', request=request),
        'tasks': reverse('project:task-list', request=request),
    })


class ProjectList(generics.ListCreateAPIView):

    model = Project
    queryset = Project.objects.all()  # .order_by.order_by('is_active', 'name')
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Project
    queryset = Project.objects.all().order_by('is_active', 'name')
    serializer_class = ProjectSerializer


class StageList(generics.ListCreateAPIView):

    model = Stage
    queryset = Stage.objects.all().order_by('is_active', 'name')
    serializer_class = StageSerializer


class StageDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Stage
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class TaskList(generics.ListCreateAPIView):

    model = Task
    queryset = Task.objects.all().order_by('is_active', 'name')
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Task
    queryset = Stage.objects.all()
    serializer_class = TaskSerializer
