from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'firstname',
            'lastname',
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone',
        )
        model = models.Student
