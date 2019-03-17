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

from django.urls import re_path
import project.views as project

app_name = 'project'

urlpatterns = [

    re_path('^project/create/$', project.ProjectCreateView.as_view(), name='project_create'),
    re_path('^project/read/$', project.ProjectListView.as_view(), name='project_read'),
    re_path('^project/read/(?P<page>\d+)/$', project.ProjectListView.as_view(), name='project_read'),
    re_path('^project/update/(?P<pk>\d+)/$', project.ProjectUpdateView.as_view(), name='project_update'),
    re_path('^project/delete/(?P<pk>\d+)/$', project.ProjectDeleteView.as_view(), name='project_delete'),
    re_path('^project/recover/(?P<pk>\d+)/$', project.ProjectRecoverView.as_view(), name='project_recover'),

]
