import os

from rest_framework import serializers



class User:

    def __init__(self, username, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    email = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        return instance


data = {'username': 'tr1nz', 'first_name': 'misha', 'last_name': 'shisha', 'email': 'mishashisha123'}
serializer = UserSerializer(data=data)
serializer.is_valid()
user = serializer.save()
print(user.username, user.first_name, user.last_name, user.email)
