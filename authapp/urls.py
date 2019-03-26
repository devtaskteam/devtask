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
import authapp.views as views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from authapp.views import UserList, UserDetail

app_name = 'authapp'

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^register/$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
