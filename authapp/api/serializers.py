from authapp.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.ImageField(use_url=True, allow_empty_file=True, max_length=None, required=False)
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'url',
            'name',
            'email',
            'password',
            'position',
            'role',
            'is_active',
            'avatar',
            'username',
        )  # '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])

        try:
            user.avatar = validated_data['avatar']
        except KeyError:
            pass

        user.save()
        return user

