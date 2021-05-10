from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'author_detail', 'created', 'updated', 'body')

class UserSerializer(serializers.ModelSerializer):
    post_detail = NestedPostSerializer(read_only=True, many=True, source='post_set')
    class Meta:
        model = User
        fields = ('id', 'username', 'post_set', 'post_detail')