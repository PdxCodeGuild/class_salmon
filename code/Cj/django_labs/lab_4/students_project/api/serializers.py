from rest_framework import serializers
from django.contrib.auth import get_user_model

from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone',
        )
        model = Students
