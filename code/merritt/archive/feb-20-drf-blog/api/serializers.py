from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'password', 'email')
        model = User

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'created')
        model = Post

class UserSerializer(serializers.ModelSerializer):
    post_set = NestedPostSerializer(read_only=True, many=True)
    class Meta:
        fields = ('id', 'username', 'email', 'post_set')
        model = User

class PostSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source="author")
    class Meta:
        fields = ('id', 'author', 'author_detail', 'title', 'body', 'created')
        model = Post