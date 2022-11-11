from profiles.models.user import User
from profiles.models.client import Client
from profiles.models.coach import Coach

from rest_framework import serializers
from rest_framework.validators import ValidationError

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
    user = UserSerializer(many=False)
           
    class Meta:
        model = Coach
        fields = ("user", "biography")

    def validate(self, attrs):
        # email_exists = User.objects.filter(email=attrs['email']).exists()
        # print(email_exists)
        
        # if email_exists:
        #     raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        print(user_data)
        coach = Coach.objects.create(**validated_data)
        print(coach)
        User.objects.create(coach=coach, **user_data)
        return coach

class ClientSingUpSerializer(serializers.ModelSerializer):
    pass
    # email = serializers.CharField(max_length = 80)
    # username = serializers.CharField()
    # password = serializers.CharField(write_only = True)
           
    # class Meta:
    #     model = User
    #     fields = ("email", "username", "password")

    # def validate(self, attrs):
    #     email_exists = User.objects.filter(email=attrs['email']).exists()
        
    #     if email_exists:
    #         raise ValidationError("Email has already been used")

    #     return super().validate(attrs)

    # def create(self, validated_data):
    #     password = validated_data.pop("password")

    #     user = super().create(validated_data)

    #     user.set_password(password) 

    #     user.is_client = True

    #     user.save()

    #     return user
