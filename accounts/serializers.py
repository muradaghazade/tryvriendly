from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'user_type')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'user_type')


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['full_name'],
                                        validated_data['email'],
                                        validated_data['password']
                                    )

        user.user_type.add(*validated_data['user_type'])

        return user
