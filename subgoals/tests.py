
import pytest
from subgoals.models import SubGoal
from goals.models import Goal
from teams.models import Team

@pytest.mark.django_db
class TestSubGoalViewSet:
    
    def test_criar_subgoal(self, usuario_logado):
        """Testa criar subtask"""
        api_client, usuario = usuario_logado
        
        team = Team.objects.create(name='Time A', owner=usuario)
        goal = Goal.objects.create(
            team=team,
            title='Meta 1',
            deadline='2025-12-31'
        )
        
        data = {
            'goal': goal.id,
            'title': 'Subtask 1',
            'description': 'Descrição'
        }
        response = api_client.post('/api/subgoals/', data, format='json')
        assert response.status_code == 201
    
    def test_completar_subgoal(self, usuario_logado):
        """Testa completar subtask"""
        api_client, usuario = usuario_logado
        
        team = Team.objects.create(name='Time A', owner=usuario)
        goal = Goal.objects.create(team=team, title='Meta 1', deadline='2025-12-31')
        subtask = SubGoal.objects.create(
            goal=goal,
            title='Subtask 1',
            assigned_to=usuario
        )
        
        response = api_client.post(f'/api/subgoals/{subtask.id}/complete/')
        assert response.status_code == 200
        assert response.data['is_completed'] == True