from message.models import Chat, Message
from authapp.models import User
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    DIALOG = 'D'
    CHAT = 'C'
    url = serializers.HyperlinkedIdentityField(view_name='message:chat-detail')

    variant = serializers.ChoiceField(choices=[
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))])
    members = serializers.HyperlinkedRelatedField(
        label='Участник',
        queryset=User.objects.all(),
        view_name='api:user-detail',
        many=True
    )

    class Meta:
        model = Chat
        fields = ('url', 'variant', 'members')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="message:message-detail")
    chat = serializers.HyperlinkedRelatedField(
        label='Название чата',
        queryset=Chat.objects.all(),
        view_name='message:chat-detail'
    )

    author = serializers.HyperlinkedRelatedField(
        label='Ползователи',
        queryset=User.objects.all(),
        view_name='api:user-detail'
    )

    class Meta:
        model = Message
        fields = '__all__'
