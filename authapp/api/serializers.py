from authapp.models import User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api_reg:user-detail")
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    # password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'url',
            'name',
            'email',
            'password',
            # 'password2',
            'position',
            'role',
            'is_active',
            'avatar',
            'username',
        )  # '__all__'  # ('email', 'name', 'password')

