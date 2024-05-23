from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo, AddStep, Category, File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed']
        extra_kwargs = {'description': {'required': False}, 'title': {'required': False}}

class AddStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddStep
        fields = ['id', 'title', 'completed']
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'choice']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file']
