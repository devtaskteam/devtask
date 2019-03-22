from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from project.api.serializers import ProjectSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from project.models import Project, Stage, Task


@api_view(['GET'])
def api_root(request):

    return Response({
        'projects': reverse('project:project-list', request=request),
    })


class ProjectList(generics.ListCreateAPIView):

    model = Project
    queryset = Project.objects.all().order_by('is_active', 'name')
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



# class ProjectCreateView(CreateView):
#
#     model = Project
#     template_name = 'project/project_update.html'
#     success_url = reverse_lazy('project:project_read')
#     # form_class = ProjectCreateForm  # вопрос: будет ли форма или на фронте как-то все будет
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'project/create'
#         return context


# class ProjectListView(viewsets.ModelViewSet):
#
#     queryset = Project.objects.all().order_by('status', 'name')
#     serializer_class = ProjectSerializer
    # template_name = 'project/project_index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'project/read'
    #     return context


# class ProjectUpdateView(UpdateView):
#     model = Project
#     template_name = 'project/project_update.html'
#     success_url = reverse_lazy('project:project_read')
#     # form_class = ProjectUpdateForm  # вопрос: будет ли форма или на фронте как-то все будет
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'project/update'
#         return context
#
#
# class ProjectDeleteView(DeleteView):
#     model = Project
#     template_name = 'project/project_delete.html'
#     success_url = reverse_lazy('project:project_read')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = False
#         self.object.save()
#
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'project/delete'
#         return context
#
#
# class ProjectRecoverView(DeleteView):
#     model = Project
#     template_name = 'project/project_delete.html'
#     success_url = reverse_lazy('project:project_read')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = True
#         self.object.save()
#
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'project/recover'
#         return context
