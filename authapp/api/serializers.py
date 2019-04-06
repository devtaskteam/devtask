from authapp.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
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
        user.save()
        return user

