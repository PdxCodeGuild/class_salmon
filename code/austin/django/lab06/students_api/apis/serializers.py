from rest_framework import serializers
from django.contrib.auth import get_user_model
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'