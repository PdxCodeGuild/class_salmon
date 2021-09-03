from rest_framework import serializers
from students.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Students
