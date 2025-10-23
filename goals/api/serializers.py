from rest_framework import serializers
from .models import Goal
from users.models import CustomUser

class GoalSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name", read_only=True)
    subtasks_count = serializers.SerializerMethodField()
    contributions_count = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = [
            'id',
            'team',
            'team_name',
            'title',
            'description',
            'deadline',
            'status',
            'created_at',
            'updated_at',
            'subtasks_count',
            'contributions_count',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'team_name', 'subtasks_count', 'contributions_count']

        def get_subtasks_count(self, obj):
            return obj.subtasks.count()
        
        def get_contributions_count(self, obj):
            return obj.contributions.count()
        