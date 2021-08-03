from rest_framework import serializers
from django.contrib.auth import get_user_model

from students_app.models import Students

class NestedStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone_url')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class StudentsSerializer(serializers.ModelSerializer):
    username_detail = NestedUserSerializer(read_only=True, source='username')
    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone_url', 'username_detail')

class UserSerializer(serializers.ModelSerializer):
    students_detail = NestedStudentsSerializer(read_only=True, many=True, source='students_set')
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'date_joined', 'students_set', 'students_detail')