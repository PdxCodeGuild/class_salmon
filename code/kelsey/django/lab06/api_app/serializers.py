from rest_framework import serializers
from django.contrib.auth import get_user_model

from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    student_detail = get_user_model()
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name', 
            'cohort', 
            'favorite_topic', 
            'favorite_teacher', 
            'capstone'
        )