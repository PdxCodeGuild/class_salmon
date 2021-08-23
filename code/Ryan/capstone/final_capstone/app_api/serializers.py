from rest_framework import serializers
from app_nfl import models
from app_squares import models
from app_users import models

class NFLSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "teamName",
            "logo",
            "win",
            "loss",
            "draw"
        )
        model = models.Team

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

        )
        model. = models.Schedule

class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (

        )
        model = models.Square

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (


        )
        model = models.Cell
