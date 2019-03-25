from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from rest_framework import viewsets

from .forms import UserRegistrationForm
from .api.serializers import UserSerializer


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
