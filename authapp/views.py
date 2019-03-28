from authapp.api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import PasswordResetView

from django.urls import reverse


from authapp.models import User


@api_view(['GET'])
def api_root(request):
    return Response({
        'login': reverse('rest_login', request=request),
        'logout': reverse('rest_logout', request=request),
        'users': reverse('api:user-list', request=request),
        'projects': reverse('project:project-list', request=request),
        'stages': reverse('project:stage-list', request=request),
        'tasks': reverse('project:task-list', request=request),
        'rest_password_reset': reverse('rest_password_reset', request=request),
        'rest_password_reset_confirm': reverse('rest_password_reset_confirm', request=request),
        'rest_password_change': reverse('rest_password_change', request=request),
        # 'user': reverse('rest_user_details', request=request),

    })


# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all().order_by('is_active', 'name')
    serializer_class = UserSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    model = User
    queryset = User.objects.all().order_by('is_active', 'name')
    serializer_class = UserSerializer

