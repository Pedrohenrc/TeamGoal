from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
from goals.models import Goal
from .serializers import GoalSerializer
from teams.models import Team

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(
            Q(team__owner=user) | Q(team__members=user)
        ).distinct()
    
    def perform_create(self, serializer):
        team_id = self.request.data.get('team')
        team = get_object_or_404(Team, id=team_id)

        if team.owner != self.request.user and self.request.user not in team.members:
            raise PermissionError("Você não tem permissão para essa ação")
        
        serializer.save()

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        goal = self.get_object()
        
        if goal.fechar_meta():
            return Response(
                {'message': 'Goal fechada com sucesso'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Existem subtasks pendentes'},
                status=status.HTTP_400_BAD_REQUEST
            )