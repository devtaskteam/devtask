from message.models import Chat  # , Message
from authapp.models import User
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    DIALOG = 'D'
    CHAT = 'C'
    url = serializers.HyperlinkedIdentityField(view_name='message:chat-detail')
    # type = serializers.CharField(source='get_type_display')
    type = serializers.ChoiceField(choices=[
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))])
    members = serializers.HyperlinkedRelatedField(
        label='Участник',
        queryset=User.objects.all(),
        view_name='api:user-detail'
    )

    class Meta:
        model = Chat
        fields = ('url', 'type', 'members')

    def create(self, validated_data):
        chat = Chat(
            members=validated_data['user_id'],
        )
        chat.members.set()  # (validated_data['members'])
        chat.save()
        return chat


# class MessageSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="project:task-detail")
#     id_project = serializers.HyperlinkedRelatedField(
#         label='Название проекта',
#         queryset=Project.objects.all(),
#         view_name='project:project-detail'
#     )
#
#     id_stage = serializers.HyperlinkedRelatedField(
#         label='Название этапа',
#         queryset=Stage.objects.all(),
#         view_name='project:stage-detail'
#     )
#
#     id_user = serializers.HyperlinkedRelatedField(
#         label='Ползователи',
#         queryset=User.objects.all(),
#         view_name='api:user-detail'
#     )
#
#     class Meta:
#         model = Message
#         fields = '__all__'
