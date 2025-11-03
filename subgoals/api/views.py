# subgoals/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import SubGoal
from .serializers import SubGoalSerializer
from goals.models import Goal

class SubGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SubGoalSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return SubGoal.objects.filter(
            Q(goal__team__owner=user) | Q(goal__team__members=user)
        ).distinct()
    
    def perform_create(self, serializer):
        goal_id = self.request.data.get('goal')
        goal = get_object_or_404(Goal, id=goal_id)
        
        user = self.request.user
        if goal.team.owner != user and user not in goal.team.members.all():
            raise PermissionError('Você não tem permissão para criar subtasks neste goal')
        
        serializer.save()
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        subtask = self.get_object()
        
        if subtask.is_completed:
            return Response(
                {'message': 'Subtask já estava completa'},
                status=status.HTTP_200_OK
            )
        
        subtask.fechar_subtask()
        
        return Response(
            SubGoalSerializer(subtask).data,
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'])
    def uncomplete(self, request, pk=None):
        subtask = self.get_object()
        subtask.is_completed = False
        subtask.save()
        
        return Response(
            SubGoalSerializer(subtask).data,
            status=status.HTTP_200_OK
        )