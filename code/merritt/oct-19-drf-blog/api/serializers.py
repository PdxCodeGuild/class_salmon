from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    author_detail = UserSerializer(read_only=True, source="author")
    class Meta:
        model = Post
        fields = ('id', 'author', 'author_detail', 'title', 'body', 'created')