from rest_framework import serializers
from students import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            "fname",
            "lname",
            "cohort",
            "fav_topic",
            "fav_teacher",
            "capstone"
        )
        model = models.Student
