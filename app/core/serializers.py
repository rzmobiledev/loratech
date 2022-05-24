from rest_framework import serializers
from core.models import User


"""
Register serializer for registering new user
to database. This serializer is exported to core.views file
"""
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    """
    This method is compulsory as django model is
    unable to hashing password. So we need to set
    and hash password within serializer forms
    """
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


"""
This serializer is only for testing 
and not be used in deployment
"""
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')

        read_only_fields = ['token']