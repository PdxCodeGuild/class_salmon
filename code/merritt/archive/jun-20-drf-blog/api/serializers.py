from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created', 'updated']

class PostSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'author_detail', 'created', 'updated']

class UserSerializer(serializers.ModelSerializer):
    post_set = NestedPostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'post_set']