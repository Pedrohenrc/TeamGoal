from rest_framework import serializers
from .models import Goal
from users.models import CustomUser

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            
        ]