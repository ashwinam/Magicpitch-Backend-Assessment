from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'username',
                  'password', 'first_name', 'last_name', 'referral_code', 'referred_by']


class UserSerializer(BaseUserSerializer):
    name = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        fields = ['name', 'email', 'referral_code', 'timestamp']

    def get_name(self, obj):
        if obj.first_name and obj.last_name:
            return f'{obj.first_name} {obj.last_name}'
        return obj.username
