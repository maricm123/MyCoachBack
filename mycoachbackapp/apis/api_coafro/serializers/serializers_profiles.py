from profiles.models.user import User
from profiles.models.client import Client
from profiles.models.coach import Coach
# from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Coach
        fields = ['id', 'biography', 'user']

class CoachSingUpSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
           
    class Meta:
        model = User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_coach=True
        user.save()
        Coach.objects.create(user=user)
        return user

class ClientSingUpSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
           
    class Meta:
        model = User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_client=True
        user.save()
        Client.objects.create(user=user)
        return user