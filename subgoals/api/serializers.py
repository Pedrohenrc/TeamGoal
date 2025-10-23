from rest_framework import serializers
from .models import SubGoal

class SubGoalSerializer(serializers.ModelSerializer):
    goal_title = serializers.CharField(source='goal.title', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True, allow_null=True)
    contributions_count = serializers.SerializerMethodField()

    class Meta:
        model = SubGoal
        fields = [
            'id',
            'goal',
            'goal_title',
            'title',
            'description',
            'is_completed',
            'assigned_to',
            'assigned_to_username',
            'created_at',
            'updated_at',
            'contributions_count'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at','goal_title', 'assigned_to_username', 'contributions_count']

        def get_contributions_count(self, obj):
            return obj.contributions.count()
        