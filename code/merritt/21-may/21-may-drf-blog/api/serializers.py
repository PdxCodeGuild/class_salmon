from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models import Post

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'author_detail', 'created', 'updated', 'body')

class UserSerializer(serializers.ModelSerializer):
    post_detail = NestedPostSerializer(read_only=True, many=True, source='post_set')
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'date_joined', 'post_set', 'post_detail')