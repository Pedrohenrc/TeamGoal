from rest_framework import serializers
from contributions.models import Contribution
from users.models import CustomUser

class ContributionSerializer(serializers.ModelSerializer):
    subgoal_title = serializers.CharField(source='subtask.title', read_only=True, allow_null=True)
    goal_title = serializers.CharField(source='goal.title', read_only=True, allow_null=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Contribution
        fields = [
            'id',
            'subtask',
            'subgoal_title',
            'goal',
            'goal_title',
            'created_at',
            'user',
            'user_username',
            'progress',
        ]
        read_only_fields = ['id', 'subgoal_title', 'goal_title', 'created_at', 'user_username']