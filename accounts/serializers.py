from rest_framework import serializers
from .models import User, CreateIvent
from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from rest_framework.views import APIView
from rest_framework.response import Response


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

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style = { 'input_type': 'password' }, trim_whitespace = False
    )

    def validate(self, data):
        print(data)
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if User.objects.filter(email = email).exists():
                user = authenticate(request = self.context.get('request'), email= email, password = password)
            else:
                msg = {
                    'detail' : 'User Not Found',
                    'status' : False,
                }
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail' : 'Does Not Exist',
                    'status' : False,
                }
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = {
                    'detail' : 'Not Found',
                    'status' : False,
            }
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data

class CreateEvent(serializers.ModelSerializer):
    class Meta:
        model = CreateIvent
        fields = ('public_id', 'event_name', 'date_created')

class GetRoomViews(APIView):

    def post(self,request):
        user = User.objects.get(email=request.user.email)
        if user.exists():
            query = GetRooms.objects.all()
            serializer = GetRoomSerializers(query, many=True)

            return Response(serializer.data)

        else:

            return Response({"error":"User does not exists"})

class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(password=value).exists():
            raise serializers.ValidationError({"password": "This password is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.password = validated_data['password']

        instance.save()

        return instance
