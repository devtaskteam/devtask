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
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework.authtoken import views as views

urlpatterns = [

    path('dashboard/', admin.site.urls),

    re_path(r'^project/', include('project.urls', namespace='project')),

    re_path('^api/', include('rest_framework.urls', namespace='api')),

    url(r'^api-token-auth/', views.obtain_auth_token),

    re_path('^api/reg/', include('authapp.urls', namespace='api_reg')),

    re_path(r'^auth/verify/social/', include("social_django.urls", namespace="social")),
    re_path(r'^social/', include('auth_social.urls', namespace='social_view')),
]
