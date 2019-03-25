from authapp.api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from authapp.models import User


@api_view(['GET'])
def api_root(request):
    return Response({
        'login': reverse('api:login', request=request),
        'logout': reverse('api:logout', request=request),
        'users': reverse('api_reg:user-list', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
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


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
