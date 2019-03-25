from authapp.api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from authapp.models import User


@api_view(['GET'])
def api_root(request):
    return Response({
        'login': reverse('api:login', request=request),
        'logout': reverse('api:logout', request=request),
        'users': reverse('api_reg:user-list', request=request),
        # 'projects': reverse('project', request=request),
    })


class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()  # .order_by.order_by('is_active', 'name')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    model = User
    queryset = User.objects.all()  # .order_by('is_active', 'name')
    serializer_class = UserSerializer
