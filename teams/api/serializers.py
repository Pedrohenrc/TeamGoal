from rest_framework import serializers
from teams.models import Team
from users.models import CustomUser

class TeamSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    members_username = serializers.SerializerMethodField()

    goals_count = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'owner_username',
            'members',
            'members_username',
            'goals_count',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'owner_username', 'members_username', 'goals_count']

    def get_goals_count(self, obj):
            return obj.goals.count()
        
    def get_members_username(self, obj):
            return [member.username for member in obj.members.all()]
        

