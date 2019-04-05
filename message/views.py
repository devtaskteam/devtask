from message.api.serializers import ChatSerializer, MessageSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from message.models import Chat, Message


@api_view(['GET'])
def api_root(request):

    return Response({
        'main': reverse('api:user-list', request=request),
        'messages': reverse('message:message-list', request=request),
        'chats': reverse('message:chat-list', request=request),

    })


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class ChatList(generics.ListCreateAPIView):

    model = Chat
    queryset = Chat.objects.all().order_by('id')
    serializer_class = ChatSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class ChatDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Chat
    queryset = Chat.objects.all().order_by('id')
    serializer_class = ChatSerializer

#  ---------------------------------------------------------------------------------------------


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class MessageList(generics.ListCreateAPIView):

    model = Message
    queryset = Message.objects.all().order_by('pub_date')
    serializer_class = MessageSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):

    model = Message
    queryset = Message.objects.all().order_by('pub_date')
    serializer_class = MessageSerializer



