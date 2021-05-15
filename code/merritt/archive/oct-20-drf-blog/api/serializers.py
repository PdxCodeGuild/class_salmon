from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'updated')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Post
        fields = ('id', 'author', 'author_detail', 'title', 'body', 'created', 'updated')

class UserSerializer(serializers.ModelSerializer):
    post_set = NestedPostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'post_set')