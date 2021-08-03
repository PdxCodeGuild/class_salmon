from rest_framework import serializers

from students_app.models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone_url']#order matters for how it returns in the JSON