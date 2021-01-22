# from rest_framework import serializers
# from .models import User
# from django.contrib.auth import authenticate

# # User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     full_name = serializers.CharField(write_only=True)


#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'password')

# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     full_name = serializers.CharField(write_only=True)


#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'password')


#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['full_name'], validated_data['email'], validated_data['password'])

#         return user
