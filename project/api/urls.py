"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import re_path
import project.views as views
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from project.views import ProjectList, ProjectDetail, StageList, StageDetail, TaskList, TaskDetail

app_name = 'project'

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^projects/$', ProjectList.as_view(), name='project-list'),
    url(r'^projects/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project-detail'),
    url(r'^stages/$', StageList.as_view(), name='stage-list'),
    url(r'^stages/(?P<pk>\d+)/$', StageDetail.as_view(), name='stage-detail'),
    url(r'^tasks/$', TaskList.as_view(), name='task-list'),
    url(r'^tasks/(?P<pk>\d+)/$', TaskDetail.as_view(), name='task-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
