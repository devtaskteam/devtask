from authapp.api.serializers import UserSerializer
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework.status import HTTP_401_UNAUTHORIZED
# from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_auth.views import PasswordResetView
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


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

# class CustomPasswordResetView(PasswordResetView):
#     """
#     Calls Django Auth PasswordResetForm save method.
#
#     Accepts the following POST parameters: email
#     Returns the success/fail message.
#     """
#     serializer_class = PasswordResetSerializer
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         # Create a serializer with request.data
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         data = request.data
#         print(data)
#         verify_link = reverse('auth:password_reset_confirm')  # , kargs={'uid': data.uid, 'token': data.token})
#         title = f'Подтверждение учетной записи {data}'
#         message = f'Для подтверждения учетной записи {data} на портале \
#            {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
#         print(verify_link, message, settings.EMAIL_HOST_USER)
#
#         serializer.save()
#
#         # Return the success message with OK HTTP status
#         return Response(
#             {"detail": _("Password reset e-mail has been sent.")},
#             status=status.HTTP_200_OK
#         ), send_mail(title, message, settings.EMAIL_HOST_USER, [data], fail_silently=False)
